from flask import Flask, render_template, redirect, url_for, request, jsonify, flash
from werkzeug.security import generate_password_hash
from config import Config
from models import db, Profile, Skill, Category, User, Field
from forms import UpdateProfileForm, RegistrationForm, LoginForm
from flask_wtf import CSRFProtect
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.utils import secure_filename
from flask import send_from_directory
import os


app = Flask(__name__)
app.config.from_object(Config)

app.config['UPLOADED_AVATARS_DEST'] = os.path.join(os.path.realpath('.'), 'uploads')
    
# Initialize CSRF protection
csrf = CSRFProtect(app)
csrf.init_app(app)

# Initialize the database
db.init_app(app)
    
# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Define a user loader callback
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    return render_template('ProConnect.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    form = UpdateProfileForm()
    fields = Field.query.all()
    fields_data = [
        {
            'id': field.id,
            'name': field.name,
            'categories': [{'id': category.id, 'name': category.name} for category in field.categories]
        }
        for field in fields
    ]
    return render_template('dashboard.html', logged_in=current_user.is_authenticated, form=form, fields_data=fields_data)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOADED_AVATARS_DEST'], filename)

@app.route('/get_categories_by_field', methods=['GET'])
def get_categories_by_field():
    field_id = request.args.get('field_id')
    categories = Category.query.filter_by(field_id=field_id).all()
    categories_data = [{'id': category.id, 'name': category.name} for category in categories]
    return jsonify(categories_data)

def get_field_choices():
    fields = Field.query.all()
    return [(field.id, field.name) for field in fields] + [('other', 'Other')]

def get_category_choices():
    categories = Category.query.all()
    return [(category.id, category.name) for category in categories] + [('other', 'Other')]

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('dashboard'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))
        
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/update_profile', methods=['GET', 'POST'])
@login_required
def update_profile():
    form = UpdateProfileForm(request.form)
    form.field.choices = get_field_choices()
    form.category.choices = get_category_choices()

    if request.method == 'POST':
        if form.validate_on_submit():
            try:

                avatar_url = None
                
                if 'avatar' in request.files:
                    file = request.files['avatar']
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(app.config['UPLOADED_AVATARS_DEST'], filename))
                    avatar_url = url_for('uploaded_file', filename=filename)
                    
                category_id = form.category.data

                if category_id == 'other':
                    custom_category_name = request.form.get('category_other')
                    custom_category = Category(name=custom_category_name, field_id=field_id)
                    db.session.add(custom_category)
                    db.session.commit()
                    category_id = custom_category.id

                # Check if a profile already exists for the current user
                profile = Profile.query.filter_by(user_id=current_user.id).first()

                if profile:
                    # Update the existing profile
                    profile.name = form.name.data
                    profile.email = form.email.data
                    profile.description = form.description.data
                    profile.avatar = avatar_url
                    profile.address = form.address.data
                    profile.payment = form.payment.data
                    profile.availability = form.availability.data
                    profile.linkedin = form.linkedin.data
                    profile.github = form.github.data
                    profile.reviews = form.reviews.data
                    profile.category_id = category_id
                    

                    profile.skills.clear()
                    for key, value in request.form.items():
                        if key.startswith('skills-'):
                            _, index, field = key.split('-')
                            if field == 'skill_name':
                                new_skill = Skill(skill_name=value, profile=profile)
                                db.session.add(new_skill)
                            elif field == 'duration':
                                new_skill.duration = value
                    

                    db.session.commit()
                    return jsonify(success=True, message="Profile updated successfully!")
                else:
                    # Create a new profile
                    new_profile = Profile(
                        user_id=current_user.id,
                        name=form.name.data,
                        email=form.email.data,
                        description=form.description.data,
                        avatar=avatar_url,
                        address=form.address.data,
                        payment=form.payment.data,
                        availability=form.availability.data,
                        linkedin=form.linkedin.data,
                        github=form.github.data,
                        reviews=form.reviews.data,
                        category_id=category_id,
                        
                    )
                    db.session.add(new_profile)

                    for key, value in request.form.items():
                        if key.startswith('skills-'):
                            _, index, field = key.split('-')
                            if field == 'skill_name':
                                new_skill = Skill(skill_name=value, profile=profile)
                                db.session.add(new_skill)
                            elif field == 'duration':
                                new_skill.duration = value

                    db.session.commit()
                    return jsonify(success=True, message="Profile created successfully!")
            except Exception as e:
                print(f"An error occurred: {e}")  # Debugging line
                return jsonify(success=False, message="An error occurred", error=str(e)), 500
        else:
            errors = {field: error[0] for field, error in form.errors.items()}
            return jsonify(success=False, message="Form validation failed", errors=form.errors), 400

    return render_template('dashboard.html', form=form)


@app.route('/profiles', methods=['GET'])
def get_profiles():
    field_id = request.args.get('field_id')
    category_id = request.args.get('category')
    skill_name = request.args.get('skill')

    query = Profile.query

    if field_id:
        query = query.filter(Field.id == field_id)

    if category_id:
        query = query.filter(Profile.category_id == category_id)

    if skill_name:
        query = query.join(Skill).filter(Skill.skill_name.ilike(f'%{skill_name}%'))

    profiles = query.all()

    profiles_data = []
    for profile in profiles:
        profile_data = {
            'name': profile.name,
            'description': profile.description,
            'avatar': profile.avatar,
            'email': profile.email,
            'linkedin': profile.linkedin,
            'github': profile.github,
            'address': profile.address,
            'payment': profile.payment,
            'availability': profile.availability,
            'skills': [f'{skill.skill_name} - {skill.duration}' for skill in profile.skills],
            'reviews': profile.reviews
        }
        profiles_data.append(profile_data)

    return jsonify(profiles_data)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port='5007')
