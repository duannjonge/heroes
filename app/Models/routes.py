#creation of flask project and routes
from flask import Flask
from config import Config  # Assuming you have a 'config.py' file with a 'Config' class
from flask_sqlalchemy import SQLAlchemy

from config import db

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)  # Initialize the SQLAlchemy extension with the app