from dbconfig import db
from datetime import datetime

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