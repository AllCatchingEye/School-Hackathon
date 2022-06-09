from sqlite3 import IntegrityError
from unicodedata import category
from flask import Blueprint, jsonify, request
from app import db
from models.organisation import Organisation as Organisationmodel
from utils.user_roles import auth_required, Config
from sqlalchemy.exc import InvalidRequestError, IntegrityError

Organisation = Blueprint('organisation', __name__)


@Organisation.route('/', methods=["POST"])
@auth_required([Config.SUPERADMIN_ID])
def add_organisation():

    org = request.get_json()
    entry = Organisationmodel(org['name'])
    db.session.add(entry)
    db.session.commit()

    return jsonify(category="Success.", message=f"Organisation added.")

@Organisation.route('/', methods=["GET"])
@auth_required([Config.SUPERADMIN_ID])
def get_organisation():
    getAll = Organisationmodel.query.all()
    return jsonify([org.to_dict(only=('orgaid', 'name')) for org in getAll])


@Organisation.route('/<organisation_id>/', methods=["PATCH"])
@auth_required([Config.SUPERADMIN_ID])
def put_organisation(organisation_id):

    data = request.get_json()

    try:
        org = Organisationmodel.query.filter_by(orgaid=organisation_id).update(data)
        db.session.commit()
        result = jsonify( category="Success.", 
                message=f"Organisation with ID {organisation_id} successfully modified.") if org else (jsonify (category="Error",
                message=f"No organisation with ID: {organisation_id}"))
    except (InvalidRequestError, IntegrityError) as e:
        db.session.rollback()
        result = jsonify(category="Error", message=f"Error while editing organisation.")

    return result


@Organisation.route('/<organisation_id>/', methods=["DELETE"])
@auth_required([Config.SUPERADMIN_ID])
def delete_organisation(organisation_id):

    Organisationmodel.query.filter_by(orgaid=organisation_id).delete()
    db.session.commit()

    return jsonify( category="Success.", 
                    message=f"Organisation with ID {organisation_id} successfully deleted.") if organisation_id is None else jsonify(category="Error", 
                    message=f"No organisation with ID: {organisation_id}")