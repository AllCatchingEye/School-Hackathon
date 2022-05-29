import imp
from flask import Flask, jsonify, request, Blueprint
from flask_cors import CORS

# Initialize Database
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object("config.Config")
db = SQLAlchemy(app)

# Blueprints for better folder structure
from blueprint_example.blueprint_example import blueprint_example
from models.user import User
from models.hackathon import Hackathon
from models.organisation import Organisation
from models.roles import Roles
from models.submission import Submission
from models.token import Token



db.create_all()
migrate = Migrate(app, db)

# enable CORS
CORS(app, resources={r'*': {'origins': '*'}})

# Register needed Blueprints
app.register_blueprint(blueprint_example, url_prefix='/api/blueprint')

if __name__ == "__main__":
    app.run(port=5001, debug=True)
