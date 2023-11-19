## Running instructions:

1. Create repository in your local server.
2. Clone the repository using `git clone https://github.com/iago2900/CalendarioSimulacion.git`
3. Create your virtual environment using `virtualenv venv`
4. Init the virtual environment `venv/Scripts/activate`
5. Install the required dependencies using `pip install -r requirements.txt`
6. Run `flask run`
7. Go to http://localhost:5000 

## DDBB current structure:
 * Roles: id, role
 * Users: id, name, surname, username, hash, role_id (foreign key)
* Groups: id, name
 * Events: id, title, description, date, start_time, end_time, n_assistants, group_id (foreign key)
 * UserEvents: id, user_id (foreign key), event_id (foreign key)
 * UserGroups: id, user_id (foreign key), group_id (foreign key)

## Stack
- https://www.sqlalchemy.org/
- https://flask.palletsprojects.com/en/3.0.x/

## SQLite:
To work with SQLITE [sqlite3](https://sqlite.org/index.html) can be used. 
- `sqlite3 SIMRadar.db`

Check the schema:
- `.schema`

Perform SQL queries:
- `SELECT username, name FROM users;`