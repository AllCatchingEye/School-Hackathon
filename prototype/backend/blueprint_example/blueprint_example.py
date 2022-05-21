from flask import Blueprint, jsonify
from models.user import User
from app import db

blueprint_example = Blueprint('blueprint_example', __name__,
                        template_folder='templates')


@blueprint_example.route('/gl/')
def geti():
    items = []
    for item in db.session.query(User).all():
        del item.__dict__['_sa_instance_state']
        items.append(item.__dict__)
    return jsonify(items)