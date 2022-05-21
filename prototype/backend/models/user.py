from app import db

class User(db.Model):
    __tablename__ = "userss"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    name = db.Column(db.String(128), unique=True, nullable=False)

    def __init__(self, email):
        self.email = email