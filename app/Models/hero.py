from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from config import db

class Hero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    super_name = db.Column(db.String, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    powers = db.relationship('Power', secondary='hero_power', backref='heroes')
    powers = db.relationship('HeroPower',backref = db.backref('heroes'))
