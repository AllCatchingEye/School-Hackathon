from app import db
from sqlalchemy_serializer import SerializerMixin

class Roles(db.Model, SerializerMixin):
    __tablename__ = "roles"

    roleid = db.Column(db.Integer, primary_key=True, autoincrement=False)
    description = db.Column(db.String(6900000), unique=False, nullable=False)
    permission = db.Column(db.String(4200000), unique=False, nullable=False)

    def __init__(self, roleid, description, permission):
        self.roleid = roleid
        self.description = description
        self.permission = permission