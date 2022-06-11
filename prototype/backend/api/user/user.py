from flask import Blueprint, jsonify, request
from app import db
from models.user import User as Usermodel
from models.roles import Roles 
from flask_jwt_extended import get_jwt, get_jwt_identity
from utils.user_roles import auth_required, Config
from sqlalchemy.exc import InvalidRequestError,IntegrityError

User = Blueprint('user', __name__)


@User.route('/', methods=["GET"])
@auth_required([Config.ADMIN_ID, Config.SUPERADMIN_ID])
def get_users():
    users = None
    if get_jwt()["role"] == Config.ADMIN_ID:
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
        user = Usermodel.query.filter_by(organisation=organisation, userid=user_id).first() 
    else:
        user = Usermodel.query.filter_by(userid=user_id).first()

    return jsonify( category="Error", 
                    message=f"No User with id: {user_id}") if user is None else jsonify(
                    user.to_dict(only=(
                                'userid', 
                                'email', 
                                'organisations', 
                                'roles', 
                                'firstname', 
                                'name')))

@User.route('/<user_id>/', methods=["DELETE"])
@auth_required([Config.ADMIN_ID, Config.SUPERADMIN_ID])
def delete_user(user_id):        
    user = None                        
    organisation = get_jwt()["organisation"]    
    role = get_jwt()["role"]    
    if role == Config.ADMIN_ID:
        user = Usermodel.query.filter_by(organisation=organisation, userid=user_id).delete()
    else:
        user = Usermodel.query.filter_by(userid=user_id).delete()
    
    db.session.commit()
    return jsonify( category="Success", 
                    message=f"User deleted {user_id}") if user else jsonify(category="Error", 
                          message=f"No User with id: {user_id}")



@User.route('/<user_id>/', methods=["PATCH"])
@auth_required([Config.ADMIN_ID, Config.SUPERADMIN_ID])
def edit_user(user_id):        
    user = None                
    data_request = request.get_json()
    organisation = get_jwt()["organisation"]    
    role = get_jwt()["role"]    
    
    try:
        if role == Config.ADMIN_ID:
            user = Usermodel.query.filter_by(organisation=organisation, userid=user_id).update(data_request)
        else:
            user = Usermodel.query.filter_by(userid=user_id).update(data_request)
        
        db.session.commit()
        result = jsonify( category="Success", 
                    message=f"User edited") if user else jsonify(category="Error", 
                          message=f"No User with id: {user_id}")
    except (InvalidRequestError, IntegrityError) as e:
        db.session.rollback()
        result = (jsonify(
                    category="Error",
                    message=f"Error while editing user"), 409)

    return result




@User.route('/own/', methods=['GET'])
@auth_required([Config.ADMIN_ID, Config.SUPERADMIN_ID, Config.TEACHER_ID])
def get_own_user():
    user = Usermodel.query.filter_by(email=get_jwt_identity()).first()
    return jsonify(user.to_dict(only=(
                                'userid', 
                                'email', 
                                'organisations', 
                                'roles', 
                                'firstname', 
                                'name')))

