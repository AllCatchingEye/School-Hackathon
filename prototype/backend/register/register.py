from flask import Blueprint, jsonify,request
from models.user import User
from app import db
from sqlalchemy.exc import IntegrityError
from flask_expects_json import expects_json
from models.organisation import Organisation
from models.roles import Roles
from utils.user_roles import auth_required, Config
from flask_jwt_extended import get_jwt

Register = Blueprint('register', __name__)
register_schema = {
    'type': 'object',
    'properties': {
        'email': {'type': 'string'},
        'name': {'type': 'string'},
        'firstname': {'type': 'string'},
        'password': {'type': 'string'},
        'role': {'type': 'integer'},
        'organisation': {'type': 'integer'}
    },
    'required': ['email', 'name', 'firstname', 'password', 'role', 'organisation']
}


@Register.route('/', methods=['POST'])
@auth_required([Config.ADMIN_ID, Config.SUPERADMIN_ID])
@expects_json(register_schema) # Compares request schema with expected schema 
def create():
    """
        Creates a teacher.
    """
    valid = False
    result = jsonify(category = "Error", message="You are not allowed to send this request")

    data_request = request.get_json()
    requested_role = data_request["role"]
    if get_jwt()["role"] == Config.ADMIN_ID:
        if requested_role in [Config.ADMIN_ID, Config.TEACHER_ID]:
            valid = True
    elif get_jwt()["role"] == Config.SUPERADMIN_ID:
        if requested_role in [Config.ADMIN_ID, Config.SUPERADMIN_ID]:
            valid = True
    if valid:
        user_data = request.get_json()
        user = User(**user_data)
        db.session.add(user)
        try:
            db.session.commit()
            result = jsonify(
                    category="Success",
                    message=f"User: {user.name} with E-Mail: {user.email} created")#, 201
        except IntegrityError as e:
            db.session.rollback()
            result = jsonify(
                    category="Error",
                    message=f"error while adding user{e}")#, 409

    return result

# Testing method to add something to database
@Register.route('/add/', methods=['GET'])
def add_to_db():
    """
        Add to DB
    """
    """    role = Roles(420, "Superadmin", "Total Access")
    role = Roles(29, "Admin", "Normal Access")
    db.session.add(role)
    db.session.commit()
    role = Roles(12, "Teacher", "Teacher Access")
    db.session.add(role)
    db.session.commit()
    role = Roles(1, "User", "User Access")
    db.session.add(role)
    db.session.commit()

    organisation = Organisation("MUCDAI")
    db.session.add(organisation)
    db.session.commit()"""

    organisation = User("muc@dealer.com", "Mucdai","Mucdai", "muc", 420, 1)
    db.session.add(organisation)
    db.session.commit()

    return str(organisation)