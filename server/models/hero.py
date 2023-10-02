from dbconfig import db

class Hero(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    super_name = db.Column(db.String(255), nullable=False)

    # Define the relationship from Hero to HeroPower
    hero_powers = db.relationship('HeroPower', back_populates='hero')

    # Define the relationship from Hero to Power through HeroPower
    powers = db.relationship(
        'Power', secondary='hero_powers', back_populates='heroes')