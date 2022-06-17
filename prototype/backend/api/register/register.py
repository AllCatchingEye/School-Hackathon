from flask import Blueprint, jsonify,request, render_template
from models.user import User
from app import db,mail
from sqlalchemy.exc import IntegrityError
from flask_expects_json import expects_json
from models.organisation import Organisation
from models.roles import Roles
from utils.user_roles import auth_required, Config
from flask_jwt_extended import get_jwt
import secrets
from flask_mail import Message

Register = Blueprint('register', __name__,template_folder='mails')
register_schema = {
    'type': 'object',
    'properties': {
        'email': {'type': 'string'},
        'name': {'type': 'string'},
        'firstname': {'type': 'string'},
        'role': {'type': 'integer'},
        'organisation': {'type': 'integer'}
    },
    'required': ['email', 'name', 'firstname', 'role', 'organisation']
}


@Register.route('/', methods=['POST'])
@auth_required([Config.ADMIN_ID, Config.SUPERADMIN_ID])
@expects_json(register_schema) # Compares request schema with expected schema 
def create():
    valid = False
    result = (jsonify(category = "Error", message="You are not allowed to send this request"), 409)

    data_request = request.get_json()
    requested_role = data_request["role"]
    if get_jwt()["role"] == Config.ADMIN_ID:
        if requested_role in [Config.ADMIN_ID, Config.TEACHER_ID]:
            valid = True
    elif get_jwt()["role"] == Config.SUPERADMIN_ID:
        if requested_role in [Config.ADMIN_ID, Config.SUPERADMIN_ID]:
            valid = True
    if valid:

        # Create User with new password
        user_data = request.get_json()
        user_password = secrets.token_urlsafe(5)
        user = User(**user_data, password=user_password)    
        
        # Create E-Mail
        msg = Message('Hello', sender = 'no-reply.wirfuerschule@gmx.de', recipients = [user.email])
        msg.body = f"Hi {user.firstname}, Your Password: {user_password} arrived."
        msg.html = render_template('set-password.html', username=user.firstname, password=user_password)
            
        db.session.add(user)            
        try:
            db.session.commit()
                
            result = (jsonify(
                    category="Success",
                    message=f"User: created",
                    dataobj=user.to_dict()), 201)
            # Send E-Mail
            mail.send(msg)          
        except IntegrityError as er:
            db.session.rollback()
            result = (jsonify(
                    category="Error",
                    message=f"error while adding user {er}"), 409)
        except Exception as e:
            print(e)
    return result

# # Testing method to add something to database
# @Register.route('/add/', methods=['GET'])
# def add_to_db():
#     """
#         Add to DB
#     """
#     """
#     role = Roles(420, "Superadmin", "Total Access")
#     db.session.add(role)
#     db.session.commit()
#     role = Roles(29, "Admin", "Normal Access")
#     db.session.add(role)
#     db.session.commit()
#     role = Roles(12, "Teacher", "Teacher Access")
#     db.session.add(role)
#     db.session.commit()
#     role = Roles(1, "User", "User Access")
#     db.session.add(role)
#     db.session.commit()

#     organisation = Organisation("MUCDAI")
#     db.session.add(organisation)
#     db.session.commit()
#     """

#     organisation = User("muc@dealer.com", "Mucdai","Mucdai", "muc", 420, 1)
#     db.session.add(organisation)
#     db.session.commit()

#     return str(organisation)