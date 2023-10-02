from models.dbconfig import db
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

class HeroPower(db.Model):
    __tablename__ = 'hero_powers'

    id = db.Column(db.Integer, primary_key=True)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey(
        'powers.id'), nullable=False)
    strength = db.Column(db.String(255))

    # Define the relationship from HeroPower to Hero
    hero = db.relationship('Hero', back_populates='hero_powers')

    # Define the relationship from HeroPower to Power
    power = db.relationship('Power', back_populates='hero_powers')

    @validates('strength')
    def validate_strength(self, key, strength):
        if strength not in ['Strong', 'Weak', 'Average']:
            raise ValueError(
                "Strength must be one of 'Strong', 'Weak', or 'Average'")
        return strength