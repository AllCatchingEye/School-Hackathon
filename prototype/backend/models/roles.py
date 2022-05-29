from app import db

class Roles(db.Model):
    __tablename__ = "roles"

    roleid = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(6900000), unique=False, nullable=False)
    permission = db.Column(db.String(4200000), unique=False, nullable=False)

    def __init__(self, description, permission):
        self.description = description
        self.permission = permission