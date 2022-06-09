from app import db
from sqlalchemy_serializer import SerializerMixin

class Hackathon(db.Model, SerializerMixin):
    __tablename__ = "hackathon"

    hackathonid = db.Column(db.Integer, primary_key=True)
    organisationid = db.Column(db.Integer, db.ForeignKey('organisation.orgaid'))
    organisation = db.relationship('Organisation')
    description = db.Column(db.String(4200000), unique=False, nullable=False)

    def __init__(self, description, organisationid):
        self.description = description
        self.organisationid = organisationid