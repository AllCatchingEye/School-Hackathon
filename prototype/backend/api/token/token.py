from flask import Blueprint, jsonify, request
from models.token import Token as Tokenmodel
from models.user import User as Usermodel
from models.hackathon import Hackathon as Hackathonmodel
from utils.user_roles import auth_required, Config
from flask_jwt_extended import get_jwt_identity, get_jwt
from app import db
from flask_expects_json import expects_json


Token = Blueprint('token', __name__)
token_schema={
    'type': 'object',
    'properties': {
        'hackathon': {'type': 'integer'},
        'count': {'type': 'integer'}
    },
    'required': ['hackathon', 'count']
}


@Token.route('/', methods=['POST'])
@auth_required([Config.ADMIN_ID, Config.TEACHER_ID])
@expects_json(token_schema)
def generate_token():
    hackathon_id=request.get_json()["hackathon"]
    number_of_token=request.get_json()["count"]
    organisation  = get_jwt()["organisation"]
    is_valid = Hackathonmodel.query.filter_by(organisationid = organisation, hackathonid = hackathon_id).first()
    result= (jsonify(category="Error",message=f"Not allowed"), 401)

    if is_valid and number_of_token > 0: 
        token_list = []
        user = Usermodel.query.filter_by(email=get_jwt_identity()).first()
        for x in range(0,number_of_token):
            token = Tokenmodel(user.userid, hackathon_id)
            db.session.add(token)    
            token_list.append(token.to_dict(only=(
                                'userid', 
                                'hackathonid',
                                '-hackathon.token',
                                'tokenid')))  
        try:
            db.session.commit() 
            result = (jsonify(
                    category="Success",
                    message=f"Created {number_of_token} Token", 
                    dataobj=token_list), 201)
        except:
            db.session.rollback()
            result= (jsonify(category="Error",message=f"An Error occured."), 401)
    return result
        

@Token.route('/', methods=['GET'])
@auth_required([Config.ADMIN_ID, Config.TEACHER_ID])
def get_token():
    organisation = get_jwt()["organisation"]
    role = get_jwt()["role"]    
    user = Usermodel.query.filter_by(email=get_jwt_identity()).first()

    if role == Config.ADMIN_ID:
        tokens = Tokenmodel.query.join(Usermodel).filter_by(organisation=organisation).all()
    else:
        tokens = Tokenmodel.query.filter_by(userid = user.userid).all()
    return jsonify([token.to_dict(only=(
                                'userid', 
                                'hackathon',
                                '-hackathon.token',
                                'tokenid')) for token in tokens])


@Token.route('/<token_id>/', methods=["DELETE"])
@auth_required([Config.ADMIN_ID, Config.TEACHER_ID])
def delete_token(token_id):        
    token = None                        
    organisation = get_jwt()["organisation"]    
    role = get_jwt()["role"]    
    
    if role == Config.ADMIN_ID:
        user_in_orga = db.session.query(Usermodel.userid).filter(organisation==organisation)
        token = db.session.query(Tokenmodel).filter(Tokenmodel.tokenid == token_id, Tokenmodel.userid.in_(user_in_orga.subquery()))        
        token = token.delete(synchronize_session=False)
    else:
        user = Usermodel.query.filter_by(email=get_jwt_identity()).first()
        token = Tokenmodel.query.filter_by(tokenid = token_id, userid = user.userid ).delete()
    
    db.session.commit()
    return jsonify( category="Success", 
                    message=f"Token deleted {token_id}") if token else jsonify(category="Error", 
                          message=f"No Token with id: {token_id}")




