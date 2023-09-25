from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from config import db

class HeroPower(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String(255))  
    hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    power_id = db.Column(db.Integer, db.ForeignKey('power.id'), nullable=False)


def __repr__(self):
    return f'<HeroPower {self.strength}>'