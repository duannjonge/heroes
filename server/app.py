#!/usr/bin/env python3

from flask_migrate import Migrate
from models.dbconfig import db
from routes import create_app

# app initialization
app = create_app()

# Configure the FLASK migrations 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hero.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Flask-Migrate with the app and the database instance
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True, port=5555)