from flask import Flask, jsonify, request, Blueprint
from flask_cors import CORS

# Schema validation for json requests
from jsonschema import ValidationError

# Initialize Database
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Json-Web-Token Package
from flask_jwt_extended import JWTManager, get_jwt, create_access_token, get_jwt_identity, set_access_cookies
from datetime import datetime, timedelta, timezone

app = Flask(__name__)
app.config.from_object("config.Config")
db = SQLAlchemy(app)

# Blueprints for better folder structure
from api.register.register import Register
from api.login.login import Login
from api.logout.logout import Logout
from api.user.user import User
from api.hackathon.hackathon import Hackathon

# import database models
from models.user import User as UserModel
from models.hackathon import Hackathon as HackathonModel
from models.organisation import Organisation as OrganisationModel
from models.roles import Roles as RolesModel
from models.submission import Submission as SubmissionModel
from models.token import Token as TokenModel


db.create_all()
migrate = Migrate(app, db, compare_type=True)


# Authentication mechanism
jwt = JWTManager(app)

# enable CORS
CORS(app, resources={r'*': {'origins': '*'}})

# Register needed Blueprints
app.register_blueprint(Register, url_prefix='/api/register')
app.register_blueprint(Login, url_prefix='/api/login')
app.register_blueprint(Logout, url_prefix='/api/logout')
app.register_blueprint(User, url_prefix='/api/user')
app.register_blueprint(Hackathon, url_prefix='/api/hackathon')

# Global error handle for schema violations 
@app.errorhandler(400)
def bad_request(error):
    if isinstance(error.description, ValidationError):
        original_error = error.description
        error = jsonify(
            category="Error", 
            message=original_error.message), 400
    return error

# Using an `after_request` callback, we refresh any token that is within 30
# minutes of expiring.
@app.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity(), additional_claims={
            "role": get_jwt()["role"], 
            "organisation": get_jwt()["organisation"]})
            set_access_cookies(response, access_token)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original response
        return response

if __name__ == "__main__":
    app.run(port=5001, debug=True)
