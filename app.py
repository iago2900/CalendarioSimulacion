import os
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from models import db, Users, Roles, Logs, Groups, Events, UserEvents
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
    user_id = session['user_id']

    return render_template("index.html", events=events, user_id=user_id)


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
        elif not request.form.get("n_assistants"):
            return apology("must provide number of assistants", 403)
        
        # Get data from new event
        title = request.form.get("title")
        description = request.form.get("description") # if empty is ""
        date = datetime.strptime(request.form.get("date"),'%Y-%m-%d').date()
        start_time = datetime.strptime(request.form.get("start_time"), "%H:%M").time()
        end_time = datetime.strptime(request.form.get("end_time"), "%H:%M").time()
        group_id = request.form.get("group") # if empty is None
        n_assistants = request.form.get("n_assistants")

        # Update DDBB
        new_event = Events(title=title, description=description, date=date, start_time=start_time, end_time=end_time, group_id=group_id, n_assistants=n_assistants)
        # Add the event to the database
        db.session.add(new_event)
        db.session.commit()

        return redirect("/")


@app.route("/add_user_event", methods=['POST'])
@login_required
def add_user_event():

    user_id = request.json.get('user_id')  
    event_id = request.json.get('event_id')
    
    # Verify if there is already a log with same user_id and event_id
    existing_log = UserEvents.query.filter_by(user_id=user_id, event_id=event_id).first()
    
    if existing_log:
        return jsonify({"message": "El log ya existe"})
    
    new_user_event = UserEvents(user_id=user_id, event_id=event_id)
    db.session.add(new_user_event)
    db.session.commit()
    
    return jsonify({"message": "Evento de usuario agregado exitosamente"})

@app.route('/delete_user_event', methods=['DELETE'])
@login_required
def delete_user_event():
    user_id = request.json.get('user_id')  
    event_id = request.json.get('event_id')
    
    # Buscar el log en la base de datos
    log_to_delete = UserEvents.query.filter_by(user_id=user_id, event_id=event_id).first()
    
    if log_to_delete:
        db.session.delete(log_to_delete)
        db.session.commit()
        return jsonify({"message": "Log eliminado exitosamente"})
    else:
        return jsonify({"message": "No se encontró el log"})


@app.route('/obtener_participantes/<int:event_id>')
@login_required
def obtener_participantes(event_id):
    participantes = db.session.query(Users).join(UserEvents).filter(UserEvents.event_id == event_id).all()

    return jsonify([{'id': participante.id, 'nombre': participante.name} for participante in participantes])


@app.route('/obtener_estado_participacion/<int:event_id>/<int:user_id>')
@login_required
def obtener_estado_participacion(event_id, user_id):
    user_event = UserEvents.query.filter_by(event_id=event_id, user_id=user_id).first()
    return jsonify({'participa': user_event is not None})

@app.route("/create-group", methods=["GET", "POST"])
@login_required
def create_group():
    if request.method == "GET":
        return render_template("create_group.html")
    else:
        if not request.form.get("name"):
            return apology("must provide a group name", 403)
        
        name = request.form.get("name")

        new_group = Groups(name=name)
        db.session.add(new_group)
        db.session.commit()

        return redirect("/")

@app.route("/assign-roles", methods=["GET", "POST"])
@login_required
def assign_roles():
    if request.method == "GET":
        users = [(user.id, user.name, user.surname) for user in Users.query.all()]
        roles = [(role.id, role.role) for role in Roles.query.all()]

        return render_template("assign_roles.html", users=users, roles=roles)
    else:
        if not request.form.get("username"):
            return apology("must provide username", 403)
        elif not request.form.get("role"):
            return apology("must provide role", 403)
        
        user_id = request.form.get("username")
        role_id = request.form.get("role")

        # Find the user
        user = Users.query.filter_by(id=user_id).first()

        if not user:
            return apology("user not found", 403)
        
        # Update the role_id
        user.role_id = role_id
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
            new_user = Users(name=request.form.get("name"), surname=request.form.get("surname"), username=request.form.get("username"), hash=generate_password_hash(request.form.get("password")), role_id=3) # Role is user by default

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