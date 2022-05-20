import imp
from flask import Flask, jsonify, request, Blueprint
from flask_cors import CORS
from blueprint_example.blueprint_example import blueprint_example

app = Flask(__name__)

app.register_blueprint(blueprint_example, url_prefix='/api/blueprint')

# enable CORS
CORS(app, resources={r'*': {'origins': '*'}})


@app.route('/api/ping', methods=['GET'])
def ping_pong():
    return jsonify({'ping_pong': 'sg test'})


if __name__ == "__main__":
    app.run(port=5001, debug=True)
