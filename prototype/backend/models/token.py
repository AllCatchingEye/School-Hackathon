from app import db

class Token(db.Model):
    __tablename__ = "token"

    tokenid = db.Column(db.Integer, primary_key=True)
    hackathonid = db.Column(db.Integer, db.ForeignKey('hackathon.hackathonid'))
    hackathon = db.relationship('Hackathon')

    def __init__(self, tokenid, hackathonid):
        self.tokenid = tokenid
        self.hackathonid = hackathonid