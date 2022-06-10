from flask import Blueprint, jsonify
from models.token import Token as Tokenmodel
from utils.user_roles import auth_required, Config
from flask_jwt_extended import get_jwt

Token = Blueprint('token', __name__)

@Token.route('/', methods=['GET'])
def get_token()
