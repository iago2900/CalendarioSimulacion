from flask import Flask

app = Flask(__name__)

# Load configuration environment
app.config.from_object("config.DevConfig")

from app import views