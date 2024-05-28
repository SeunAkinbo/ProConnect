from flask import Flask, render_template, redirect, url_for, request, jsonify, flash
from werkzeug.security import generate_password_hash
from config import Config
from models import db, Profile, Skill, Category, User
from forms import UpdateProfileForm, RegistrationForm, LoginForm
from flask_wtf import CSRFProtect
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config.from_object(Config)

# Store upload files
app.config['UPLOAD_FOLDER'] = os.path.realpath('.') + '/uploads'

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

@app.route('/dashboard')
def dashboard():
    form = UpdateProfileForm()
    categories = Category.query.all()
    return render_template('dashboard.html', categories=categories, form=form)

@app.route('/add_categories')
def add_categories():
    categories = ['Web Development', 'Graphic Design', 'Data Analysis', 'Project Management']
    for name in categories:
        category = Category(name=name)
        db.session.add(category)
    db.session.commit()
    return "Categories added!"

def get_category_choices():
    categories = Category.query.all()
    return [(category.id, category.name) for category in categories]

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
    return redirect(url_for('login'))
        
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
    form.category.choices = get_category_choices()

    if request.method == 'POST':
        if form.validate_on_submit():
            # Check if a file was uploaded
            if 'file' in request.files:
                file = request.files['file']
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    file.save(file_path)
                    form.avatar.data = file_path

            # Check if a profile already exists for the current user
            profile = Profile.query.filter_by(user_id=current_user.id).first()

            if profile:
                # Update the existing profile
                profile.name = form.name.data
                profile.email = form.email.data
                profile.description = form.description.data
                profile.avatar = form.avatar.data
                profile.address = form.address.data
                profile.payment = form.payment.data
                profile.availability = form.availability.data
                profile.linkedin = form.linkedin.data
                profile.github = form.github.data
                profile.reviews = form.reviews.data
                profile.category_id = form.category.data

                profile.skills.clear()
                for skill in form.skills.entries:
                    new_skill = Skill(skill_name=skill.data['skill_name'], duration=skill.data['duration'], profile=profile)
                    db.session.add(new_skill)

                db.session.commit()
                return jsonify(success=True, message="Profile updated successfully!")
            else:
                # Create a new profile
                new_profile = Profile(
                    user_id=current_user.id,
                    name=form.name.data,
                    email=form.email.data,
                    description=form.description.data,
                    avatar=form.avatar.data,
                    address=form.address.data,
                    payment=form.payment.data,
                    availability=form.availability.data,
                    linkedin=form.linkedin.data,
                    github=form.github.data,
                    reviews=form.reviews.data,
                    category_id=form.category.data
                )
                db.session.add(new_profile)

                for skill in form.skills.entries:
                    new_skill = Skill(skill_name=skill.data['skill_name'], duration=skill.data['duration'], profile=new_profile)
                    db.session.add(new_skill)

                db.session.commit()
                return jsonify(success=True, message="Profile created successfully!")
        else:
            return jsonify(success=False, message="Form validation failed", errors=form.errors), 400

    return render_template('dashboard.html', form=form)  # Render the form for GET requests

@app.route('/profiles', methods=['GET'])
def get_profiles():
    category_id = request.args.get('category')
    skill_name = request.args.get('skill')

    query = Profile.query

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
