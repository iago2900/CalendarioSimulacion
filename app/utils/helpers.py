from flask import redirect, flash
from app.models import Users
from functools import wraps
from flask_login import current_user

def permission_admin(f):
    """
    Decorator for routes that only admins can access.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user = Users.query.filter_by(id=current_user.id).first()
        if user.role_id != 1:
            flash("Access denied.", "danger")
            return redirect("/")
        return f(*args, **kwargs)
    return decorated_function