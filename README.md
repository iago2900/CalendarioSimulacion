## Running instructions:

1. Create repository in your local server.
2. Clone the repository using `git clone https://github.com/iago2900/CalendarioSimulacion.git`
3. Create your virtual environment using `virtualenv venv`
4. Init the virtual environment `venv/Scripts/activate`
5. Install the required dependencies using `pip install -r requirements.txt`
6. Run `flask run`
7. Go to http://localhost:5000 


## Redo Database
If a change to the Models has to be done you can upload again demo data through the following steps:
- Delete de current database `SIMRadar.db`
- Check if tables are in `models.py`
- Run `python create_db.py` to create new database

## DDBB current structure:
 * Users: id, name, surname, username, hash, role_id (foreign key), group_id (foreign key)
 * Roles: id, role
 * Logs: id, action, timestamp, event_id (foreign key)
 * Events: id, title, start_datetime, end_datetime, group_id (foreign key)
 * Groups: id, name

## Stack
- https://www.sqlalchemy.org/
- https://flask.palletsprojects.com/en/2.0.x/

## SQLite:
To work with SQLITE [sqlite3](https://sqlite.org/index.html) can be used. Once the database is created through `python create_db.py` open it:
- `sqlite3 SIMRadar.db`

Check the schema:
- `.schema`

Perform SQL queries:
- `SELECT username, name FROM users;`