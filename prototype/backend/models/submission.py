from app import db
from sqlalchemy_serializer import SerializerMixin

class Submission(db.Model, SerializerMixin):
    __tablename__ = "submission"

    subid = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(6900000), unique=False, nullable=False)
    hackathonid = db.Column(db.Integer, db.ForeignKey('hackathon.hackathonid'), nullable=False)
    hackathon = db.relationship('Hackathon')

    def __init__(self, description, hackathonid):
        self.description = description
        self.hackathonid = hackathonid