from flask import Blueprint, jsonify,request
from models.user import User, userschema
from app import db
from sqlalchemy.exc import IntegrityError
from flask_expects_json import expects_json

register = Blueprint('register', __name__)

@register.route('/', methods=['POST'])
@expects_json(userschema) # Compares request schema with expected schema 
def create_user():
    user_data = request.get_json()
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