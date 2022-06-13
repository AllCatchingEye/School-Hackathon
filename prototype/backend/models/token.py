from app import db
import uuid
from sqlalchemy_serializer import SerializerMixin

class Token(db.Model, SerializerMixin):
    __tablename__ = "token"

    tokenid = db.Column(db.String,  default=lambda: str(uuid.uuid4()), primary_key=True)
    hackathonid = db.Column(db.Integer, db.ForeignKey('hackathon.hackathonid'))
    hackathon = db.relationship('Hackathon')
    userid = db.Column(db.Integer, db.ForeignKey('users.userid'))

    def __init__(self, userid, hackathonid):
        self.hackathonid = hackathonid
        self.userid = userid