from config import Config
from flask import Flask
from models import db, User, Profile
import os

# Set up Flask application
app = Flask(__name__)
app.config.from_object(Config)

# Initialize the database with the app context
db.init_app(app)

def create_user(email, password):
    user = User(email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return user

def link_profiles_to_users():
    profiles = Profile.query.filter(Profile.user_id == None).all()
    
    for profile in profiles:
        # Create a user for each profile
        email = f"{profile.name.replace(' ', '_').lower()}@example.com"
        password = "defaultpassword"  # Use a default password or generate a random one

        user = create_user(email, password)
        
        # Link profile to the newly created user
        profile.user_id = user.id
        db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        link_profiles_to_users()
        print("Users created and profiles linked.")
