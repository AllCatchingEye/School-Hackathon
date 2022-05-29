from flask import Blueprint, jsonify,request
from models.user import User
from app import db
from sqlalchemy.exc import IntegrityError
from flask_expects_json import expects_json
from models.organisation import Organisation
from models.roles import Roles

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


@Register.route('/teacher/', methods=['POST'])
@expects_json(register_schema) # Compares request schema with expected schema 
def create_teacher():
    """
        Creates a teacher.
    """
    user_data = request.get_json()
    print(user_data)
    user = User(**user_data)
    db.session.add(user)
    try:
        db.session.commit()
        result = jsonify(
                category="Success", 
                message=f"User: {user.name} with E-Mail: {user.email} created"), 201
    except IntegrityError as e:
        db.session.rollback()
        result = jsonify(
                category="Error", 
                message=f"{e}"), 409
    
    return result


@Register.route('/superadmin/', methods=['POST'])
@expects_json(register_schema) # Compares request schema with expected schema 
def create_super_admin():
    """
        Creates a super admin.
    """
    pass
    


@Register.route('/admin/', methods=['POST'])
@expects_json(register_schema) # Compares request schema with expected schema 
def create_admin():
    """
        Creates an admin.
    """
    pass


# Testing method to add something to database
@Register.route('/add/', methods=['GET'])
def add_to_db():
    """
        Add to DB
    """
    role = Organisation("MUCDAI")
    db.session.add(role)
    db.session.commit()
    return str(role)