from flask import Blueprint, jsonify
from models.admin import Admin
from app import db

blueprint_example = Blueprint('blueprint_example', __name__,
                        template_folder='templates')


@blueprint_example.route('/gl/')
def geti():
    items = []
    for item in db.session.query(Admin).all():
        del item.__dict__['_sa_instance_state']
        items.append(item.__dict__)
    return jsonify(items)