from dbconfig import db

class Hero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    super_name = db.Column(db.String, unique=True, nullable=False)

    # many-to-many relationship with Power through HeroPower
    powers = db.relationship('Power', secondary='hero_power', backref='heroes')

    def __repr__(self):
        return f'<Hero {self.name}>'