from flask import Flask

app = Flask(__name__)

# Load configuration environment
app.config.from_object("config.ProductionConfig")

from app import views