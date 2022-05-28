from app import db

class Hackathon(db.Model):
    __tablename__ = "hackathon"

    hackathonid = db.Column(db.Integer, primary_key=True)
    organisationid = db.Column(db.Integer, db.ForeignKey('organisation.orgaid'))
    organization = db.relationship('Organisation')
    description = db.Column(db.String(4200000), unique=False, nullable=False)

    def __init__(self, description, permission):
        self.description = description
        self.permission = permission