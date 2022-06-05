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
from blueprint_example.blueprint_example import blueprint_example
from register.register import Register
from login.login import Login
from logout.logout import Logout
from user.user import User as UserBlueprint

from models.user import User
from models.hackathon import Hackathon
from models.organisation import Organisation
from models.roles import Roles
from models.submission import Submission
from models.token import Token


db.create_all()
migrate = Migrate(app, db, compare_type=True)


# Authentication mechanism
jwt = JWTManager(app)

# enable CORS
CORS(app, resources={r'*': {'origins': '*'}})

# Register needed Blueprints
app.register_blueprint(blueprint_example, url_prefix='/api/blueprint')
app.register_blueprint(Register, url_prefix='/api/register')
app.register_blueprint(Login, url_prefix='/api/login')
app.register_blueprint(Logout, url_prefix='/api/logout')
app.register_blueprint(UserBlueprint, url_prefix='/api/user')

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
