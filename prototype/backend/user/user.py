from flask import Blueprint, jsonify
from app import db
from models.user import User as Usermodel
from models.roles import Roles 
from flask_jwt_extended import get_jwt
from utils.user_roles import auth_required, Config

User = Blueprint('user', __name__)


@User.route('/', methods=["GET"])
@auth_required([Config.ADMIN_ID, Config.SUPERADMIN_ID])
def get_users():
    users = None
    if get_jwt()["organisation"] == Config.ADMIN_ID:
        # Only query admins and teacher of the same organization
        organisation = get_jwt()["organisation"]
        users = Usermodel.query.filter_by(organisation=organisation).join(Roles).all() 
    else:
        users = Usermodel.query.join(Roles).all()

    return jsonify([user.to_dict(only=(
                                'userid', 
                                'email', 
                                'organisations', 
                                'roles', 
                                'firstname', 
                                'name')) for user in users])


@User.route('/<user_id>/', methods=["GET"])
@auth_required([Config.ADMIN_ID, Config.SUPERADMIN_ID])
def get_user(user_id):
    user = None
    if get_jwt()["organisation"] == Config.ADMIN_ID:
        # Only query admins and teacher of the same organization
        organisation = get_jwt()["organisation"]
        user = Usermodel.query.filter_by(organisation=organisation,userid=user_id).join(Roles).first() 
    else:
        user = Usermodel.query.filter_by(userid=user_id).join(Roles).first()

    return jsonify( category="Error", 
                    message=f"No User with id: {user_id}") if user is None else jsonify(
                    user.to_dict(only=(
                                'userid', 
                                'email', 
                                'organisations', 
                                'roles', 
                                'firstname', 
                                'name')))