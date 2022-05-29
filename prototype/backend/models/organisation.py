from app import db

class Organisation(db.Model):
    __tablename__ = "organisation"

    orgaid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(6900000), unique=False, nullable=False)

    def __init__(self, name):
        self.name = name