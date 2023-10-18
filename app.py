import os
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from models import db, Users, Roles, Logs, Groups, Events
from helpers import login_required, apology

app = Flask(__name__)

app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///SIMRadar.db'
Session(app)

db.init_app(app)


@app.route("/", methods=['GET'])
@login_required
def index():
    """Show list of events"""
    events = [event for event in Events.query.all()]
    return render_template("index.html", events=events)

@app.route("/create-event", methods=["GET", "POST"])
@login_required
def create_event():
    """
    Form to create new event.
    """
    if request.method == "GET":

        groups = [(group.id, group.name) for group in Groups.query.all()]

        return render_template("create_event.html", groups=groups)
    else: #post
        
        # Ensure mandatory fields are submitted
        if not request.form.get("title"):
            return apology("must provide title", 403)
        elif not request.form.get("date"):
            return apology("must provide date", 403)
        elif not request.form.get("start_time"):
            return apology("must provide start time", 403)
        elif not request.form.get("end_time"):
            return apology("must provide end time", 403)
        
        # Get data from new event
        title = request.form.get("title")
        description = request.form.get("description") # if empty is ""
        date = datetime.strptime(request.form.get("date"),'%Y-%m-%d').date()
        start_time = datetime.strptime(request.form.get("start_time"), "%H:%M").time()
        end_time = datetime.strptime(request.form.get("end_time"), "%H:%M").time()
        group_id = request.form.get("group") # if empty is None

        # Update DDBB
        new_event = Events(title=title, description=description, date=date, start_time=start_time, end_time=end_time, group_id=group_id)
        # Add the event to the database
        db.session.add(new_event)
        db.session.commit()

        return redirect("/")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure fields are submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = Users.query.filter_by(username=request.form.get("username")).first()

        # Ensure username exists and password is correct
        if rows == None or not check_password_hash(rows.hash, request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows.id

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")

    else: # method == 'POST'

        # Ensure fields are submitted
        if not request.form.get("name"):
            return apology("must provide name", 403)

        elif not request.form.get("surname"):
            return apology("must provide surname", 403)

        elif not request.form.get("username"):
            return apology("must provide username", 400)

        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Ensure confirm_password was submitted and is the same
        elif not request.form.get("confirmation") or (request.form.get("confirmation") != request.form.get("password")):
            return apology("must confirm the password", 400)

        # Query database for username
        rows = Users.query.filter_by(username=request.form.get("username")).first()
 
        if rows == None: # Ensure username does not exist
            # Create a new user
            new_user = Users(name=request.form.get("name"), surname=request.form.get("surname"), username=request.form.get("username"), hash=generate_password_hash(request.form.get("password")))

            # Add the user to the database
            db.session.add(new_user)
            db.session.commit()

        else:
            return apology("username already exists", 400)


        # Redirect user to home page
        return redirect("/")
    

@app.route("/password", methods=["GET", "POST"])
@login_required
def password():
    """Show form to change password"""
    if request.method == "GET":
        return render_template("password.html")

    else:

        # Ensure password was submitted
        if not request.form.get("password"):
            return apology("must provide password", 403)

        # Ensure confirm_password was submitted and is the same
        elif not request.form.get("confirmation") or (request.form.get("confirmation") != request.form.get("password")):
            return apology("must confirm the password", 403)

        # Get the user you want to update
        user = Users.query.filter_by(id=session["user_id"]).first()

        # Update the user's hash
        user.hash = generate_password_hash(request.form.get("password"))

        # Commit the changes to the database
        db.session.commit()

        # Redirect user to home page
        return redirect("/")