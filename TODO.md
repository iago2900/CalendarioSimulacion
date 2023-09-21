# SQL

* Initialize SQL DDBB (copy from AIS project)
* Define tables to store data
* Create tables in SQL

  * Users: id, username, password_hashed, role_id (foreign key), group_id (foreign key)
  * Roles: id, role
  * Logs: id, action, timestamp, event_id (foreign key)
  * Activities: id, title, date 
  * Groups: id, group

# Calendar

* How to save events into DDBB
* An event must have: 
  * title
  * description
  * date
  * number of participants
  * list of the participants joined
  * group of users that can see that event

# Permissions / roles

* Admin: can add events
* User: can join an event

# Register / Login

* Check from Finance
* https://flask-login.readthedocs.io/en/latest/

# Export