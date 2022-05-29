import imp
from flask import Flask, jsonify, request, Blueprint
from flask_cors import CORS

# Schema validation for json requests
from jsonschema import ValidationError

# Initialize Database
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object("config.Config")
db = SQLAlchemy(app)

# Blueprints for better folder structure
from blueprint_example.blueprint_example import blueprint_example
from register.register import Register
from models.user import User

db.create_all()
migrate = Migrate(app, db)

# enable CORS
CORS(app, resources={r'*': {'origins': '*'}})

# Register needed Blueprints
app.register_blueprint(blueprint_example, url_prefix='/api/blueprint')
app.register_blueprint(Register, url_prefix='/api/register')


# Global error handle for schema violations 
@app.errorhandler(400)
def bad_request(error):
    if isinstance(error.description, ValidationError):
        original_error = error.description
        error = jsonify(
            category="Error", 
            message=original_error.message), 400
    return error

if __name__ == "__main__":
    app.run(port=5001, debug=True)
