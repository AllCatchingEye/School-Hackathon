from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid

app = Flask(__name__)


# enable CORS
CORS(app, resources={r'*': {'origins': '*'}})


@app.route('/api/ping', methods=['GET'])
def ping_pong():
    return jsonify({'ping_pong': 'pong test'})



if __name__ == "__main__":
    app.run(port=5001, debug=True)
