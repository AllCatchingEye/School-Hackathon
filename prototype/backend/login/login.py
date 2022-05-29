from flask import Blueprint, jsonify, request
from app import db
from flask_jwt_extended import create_access_token
from models.user import User
from flask_expects_json import expects_json

Login = Blueprint('login', __name__)
login_schema = {
    'type': 'object',
    'properties': {
        'email': {'type': 'string'},
        'password': {'type': 'string'}        
    },
    'required': ['email', 'password']
}

@Login.route("/", methods=["POST"])
@expects_json(login_schema) 
def login():
    data = request.get_json()
    user = User.authenticate(**data)
    result = None
    if not user:
        result = jsonify({"message": "Bad email or password"}), 401
    else:
        access_token = create_access_token(identity=user.email, additional_claims={
            "role": user.role, 
            "organisation": user.organisation})
        result =  jsonify(access_token=access_token), 200
    return result    





