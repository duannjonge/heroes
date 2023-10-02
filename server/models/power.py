from dbconfig import db

class Power(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False, unique=True, 
                            CheckConstraint("length(description) >= 20"))

    def __repr__(self):
        return f'<Power {self.name}>'