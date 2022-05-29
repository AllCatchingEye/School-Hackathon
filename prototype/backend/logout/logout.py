from flask import Blueprint, jsonify
from flask_jwt_extended import unset_jwt_cookies, get_jwt_identity
from utils.user_roles import auth_required, Config


Logout = Blueprint('logout', __name__)

@Logout.route("/", methods=["POST"])
@auth_required([Config.ADMIN_ID, Config.SUPERADMIN_ID, Config.TEACHER])
def logout():
    response = jsonify({"message": f"logged out {get_jwt_identity()} successful"})
    unset_jwt_cookies(response)
    return response
 
