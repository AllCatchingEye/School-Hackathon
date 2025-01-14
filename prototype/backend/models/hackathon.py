from app import db
from sqlalchemy_serializer import SerializerMixin
from urllib import parse

class Hackathon(db.Model, SerializerMixin):
    __tablename__ = "hackathon"

    hackathonid = db.Column(db.Integer, primary_key=True)
    organisationid = db.Column(db.Integer, db.ForeignKey('organisation.orgaid'))
    organisation = db.relationship('Organisation')
    description = db.Column(db.String(4200000), unique=False, nullable=False)
    title = db.Column(db.String(42000), unique=False, nullable=False)
    token = db.relationship("Token", cascade="all, delete-orphan",back_populates="hackathon")
    slug = db.Column(db.String(4200), unique=True, nullable=False)

    def __init__(self, title, description, organisationid, slug):
        self.description = description
        self.organisationid = organisationid
        self.title = title
        self.slug = parse.quote_plus(slug)