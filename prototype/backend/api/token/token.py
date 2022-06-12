from flask import Blueprint, jsonify, request
from models.token import Token as Tokenmodel
from models.user import User as Usermodel
from utils.user_roles import auth_required, Config
from flask_jwt_extended import get_jwt_identity, get_jwt
from app import db
Token = Blueprint('token', __name__)

@Token.route('/', methods=['POST'])
@auth_required([Config.ADMIN_ID, Config.TEACHER_ID])
def generate_token():
    hackathonid=request.get_json()["hackathon"]
    number_of_token=request.get_json()["count"]
    assert number_of_token > 0
    user = Usermodel.query.filter_by(email=get_jwt_identity()).first()
    for x in range(0,number_of_token):
        token = Tokenmodel(user.userid, hackathonid)
        db.session.add(token)            
    
    try:
        db.session.commit() 
    except:
        db.session.rollback()
    
    return (jsonify(
                    category="Success",
                    message=f"Created {number_of_token} Token"), 201)


@Token.route('/', methods=['GET'])
@auth_required([Config.ADMIN_ID, Config.TEACHER_ID])
def get_token():
    organisation = get_jwt()["organisation"]
    tokens = Tokenmodel.query.join(Usermodel).filter_by(organisation=organisation).all()
    return jsonify([token.to_dict(only=(
                                'userid', 
                                'hackathon',
                                '-hackathon.token',
                                'tokenid')) for token in tokens])

 