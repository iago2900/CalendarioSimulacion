## Running instructions:

1. Create repository in your local server.
2. Clone the repository using `git clone https://github.com/iago2900/CalendarioSimulacion.git`
3. Create your virtual environment using `virtualenv venv`
4. Init the virtual environment `venv/Scripts/activate`
5. Install the required dependencies using `pip install -r requirements.txt`
6. Run `python wsgi.py`

## Running instructions

- Create a virtualenvironment:
  
```python3.9 -m virtualenv venv```

- Init the virtual environment + install the requirements:

```source venv/bin/activate```

```python3.9 -m pip install -r requirements.txt```

- Run:

```python3.9 wsgi.py```

- Go to http://localhost:5000


### Redo Database
If a change to the Models has to be done you can upload again demo data through the following steps:
- Delete de current database ```db.sqlite```
- Make sure that the Models changes are reflected on models.py
- Create the database through ```create_app.py```
- Run the app through ```python3 wsgi.py```
- Upload all data by running all helpers through ```/run_all_helpers```


## Stack
- https://www.sqlalchemy.org/
- https://flask.palletsprojects.com/en/2.0.x/

### SQLite:
To work with SQLITE [sqlite3](https://sqlite.org/index.html) can be used. Once the database is created through ```python3.9 create_app.py``` open it:
- ```sqlite3 db.sqlite```

Check the schema:
- ```.schema```

Perform SQL queries:
- ```SELECT email, name FROM user;```