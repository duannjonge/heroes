from models.dbconfig import db
from sqlalchemy.orm import validates

class Power(db.Model):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)

    # Define the relationship from Power to HeroPower
    hero_powers = db.relationship('HeroPower', back_populates='power')

    # Define the relationship from Power to Hero through HeroPower
    heroes = db.relationship(
        'Hero', secondary='hero_powers', back_populates='powers')

    @validates('description')
    def validate_description(self, key, description):
        if not description or len(description) < 20:
            raise ValueError("Description must be at least 20 characters long")
        return description