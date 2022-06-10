from flask import Blueprint, jsonify
from models.roles import Roles as Rolemodel
from utils.user_roles import auth_required, Config
from flask_jwt_extended import get_jwt

Role = Blueprint('role', __name__)

@Role.route('/', methods=['GET'])
@auth_required([Config.ADMIN_ID, Config.SUPERADMIN_ID])
def get_roles():
    roles = jsonify(category = "Error", message="You are not allowed to send this request")
    
    if get_jwt()["role"] == Config.SUPERADMIN_ID:
        roles = Rolemodel.query.all() 
    else:
        filters = (Rolemodel.roleid == Config.ADMIN_ID) | (Rolemodel.roleid == Config.TEACHER_ID)
        roles = Rolemodel.query.filter(filters).all() 

    return jsonify([role.to_dict(only=(
                                    'roleid',
                                    'description',
                                    'permission'
                                    )) for role in roles])