from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy_serializer import SerializerMixin

class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    userid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    name = db.Column(db.String(128), unique=False, nullable=False)
    firstname = db.Column(db.String(128), unique=False, nullable=False)
    password = db.Column(db.String(128), unique=False, nullable=False)
    role = db.Column(db.Integer, db.ForeignKey('roles.roleid'), unique=False, nullable=False)
    roles = db.relationship('Roles')
    organisation = db.Column(db.Integer, db.ForeignKey('organisation.orgaid'),unique=False, nullable=False)
    organisations = db.relationship('Organisation')


    def __init__(self, email, name, firstname, password, role, organisation):
        self.email = email
        self.name = name
        self.firstname = firstname
        self.password = generate_password_hash(password, method='sha256')
        self.role = role
        self.organisation = organisation

    @classmethod
    def authenticate(cls, **kwargs):
        email = kwargs.get('email')
        password = kwargs.get('password')
        user = cls.query.filter_by(email=email).first()
        result = None
        if user and check_password_hash(user.password, password):
            result = user
        return result
    