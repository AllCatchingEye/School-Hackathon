from app import db
from sqlalchemy_serializer import SerializerMixin

class Organisation(db.Model, SerializerMixin):
    __tablename__ = "organisation"

    orgaid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(6900000), unique=False, nullable=False)

    def __init__(self, name):
        self.name = name