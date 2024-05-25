#!/usr/bin/python3
from flask import Flask, render_template, redirect, url_for, request, jsonify
from config import Config
from models import db, Profile, Skill
from forms import UpdateProfileForm  # Assuming you have a form defined in forms.py

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def home():
    return render_template('ProConnect.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/update', methods=['POST'])
def update_profile():
    form = UpdateProfileForm(request.form)
    if form.validate():
        profile = Profile.query.filter_by(email=form.email.data).first()
        if not profile:
            profile = Profile(
                name=form.name.data,
                description=form.description.data,
                avatar=form.avatar.data,
                address=form.address.data,
                payment=form.payment.data,
                availability=form.availability.data,
                email=form.email.data,
                linkedin=form.linkedin.data,
                github=form.github.data,
                reviews=form.reviews.data
            )
            db.session.add(profile)
        else:
            profile.name = form.name.data
            profile.description = form.description.data
            profile.avatar = form.avatar.data
            profile.address = form.address.data
            profile.payment = form.payment.data
            profile.availability = form.availability.data
            profile.linkedin = form.linkedin.data
            profile.github = form.github.data
            profile.reviews = form.reviews.data
        
        # Update skills
        profile.skills.clear()
        for skill, duration in zip(form.skills.data, form.duration.data):
            new_skill = Skill(skill_name=skill, duration=duration, profile=profile)
            db.session.add(new_skill)
        
        db.session.commit()
        return jsonify(success=True)
    return jsonify(success=False), 400

@app.route('/profiles', methods=['GET'])
def get_profiles():
    skill_name = request.args.get('skill')
    profiles = Profile.query.join(Skill).filter(Skill.skill_name.ilike(f'%{skill_name}%')).all()
    
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
    app.run(debug=True)
