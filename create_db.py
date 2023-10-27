from models import db, Roles
from app import app

def create_default_roles():
    roles = ['superadmin', 'admin', 'user']
    for role in roles:
        new_role = Roles(role=role)
        db.session.add(new_role)
    db.session.commit()

with app.app_context():
    db.create_all()
    
    # Check if roles already exist
    existing_roles = Roles.query.all()
    if not existing_roles:
        create_default_roles()