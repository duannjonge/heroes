from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from config import db

class Power(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String, nullable=False)
    description=db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    heroes = db.relationship('HeroPower', backref= db.backref('powers'))



def __repr__(self):
    return f'<Power {self.name}>'