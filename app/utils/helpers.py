from flask import redirect, session, flash
from app.models import Users
from functools import wraps


def login_required(f):
    """
    Decorate routes to require login.
    http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def permission_admin(f):
    """
    Decorator for routes that only admins can access.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user = Users.query.filter_by(id=session["user_id"]).first()
        if user.role_id != 1:
            flash("Access denied.", "danger")
            return redirect("/")
        return f(*args, **kwargs)
    return decorated_function