from flask import Blueprint, jsonify
from app import db
from models.user import User as Usermodel
from models.roles import Roles 
from flask_jwt_extended import get_jwt
from utils.user_roles import auth_required, Config

User = Blueprint('user', __name__,
                        template_folder='templates')


@User.route('/', methods=["GET"])
@auth_required([Config.ADMIN_ID, Config.SUPERADMIN_ID])
def geti():
    users = None
    if get_jwt()["organisation"] == Config.ADMIN_ID:
        organisation = get_jwt()["organisation"]
        users = Usermodel.query.filter_by(organisation=organisation).all()
    else:
        users = Usermodel.query.join(Roles).all()

    return jsonify([user.to_dict(only=(
                                'userid', 
                                'email', 
                                'organisations', 
                                'roles', 
                                'firstname', 
                                'name')) for user in users])