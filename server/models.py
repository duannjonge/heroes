from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

from config import db

class Power(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)

def __repr__(self):
    return f'<Power {self.name}>'

class Hero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    super_name = db.Column(db.String, unique=True, nullable=False)

    # Establish a many-to-many relationship with Power through HeroPower
    powers = db.relationship('Power', secondary='hero_power', backref='heroes')


def __repr__(self):
    return f'<Hero {self.name}>'

class HeroPower(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String(255))

    # Define foreign keys for Hero and Power
    hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('power.id'), nullable=False)

    # Define relationships with Hero and Power
    hero = db.relationship('Hero', backref=db.backref('hero_powers', cascade='all, delete-orphan'))
    power = db.relationship('Power')

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


def __repr__(self):
    return f'<HeroPower {self.strength}>'



