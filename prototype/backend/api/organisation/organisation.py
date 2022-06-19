from flask import Blueprint, jsonify, request
from app import db
from models.organisation import Organisation as Organisationmodel
from utils.user_roles import auth_required, Config
from sqlalchemy.exc import InvalidRequestError, IntegrityError
from flask_jwt_extended import get_jwt

Organisation = Blueprint('organisation', __name__)


@Organisation.route('/', methods=["POST"])
@auth_required([Config.SUPERADMIN_ID])
def add_organisation():

    data = request.get_json()
    organisation = Organisationmodel(**data)
    db.session.add(organisation)
    result = (jsonify(
        category="Error",
        message=f"Error while addign hackathon"), 409)
    try:
        db.session.commit()
        result = (jsonify(
                    category="Success",
                    message=f"Added Organisation {organisation.name}.",
                    dataobj=organisation.to_dict(only=(
                                'orgaid', 
                                'name'))), 201)
    except IntegrityError as e:
        result = (jsonify(
                    category="Error",
                    message=f"Organisation with name {hackathon.name} already exists"), 409)
        db.session.rollback()
    except:
        db.session.rollback()

    return result

@Organisation.route('/', methods=["GET"])
@auth_required([Config.SUPERADMIN_ID, Config.ADMIN_ID, Config.TEACHER_ID])
def get_organisation():
    role = get_jwt()["role"]    
    getAll = Organisationmodel.query.all()
    return jsonify([org.to_dict(only=('orgaid', 'name')) for org in getAll] if role ==  Config.SUPERADMIN_ID else [])


@Organisation.route('/<organisation_id>/', methods=["PATCH"])
@auth_required([Config.SUPERADMIN_ID])
def put_organisation(organisation_id):

    data = request.get_json()

    try:
        org = Organisationmodel.query.filter_by(orgaid=organisation_id).update(data)
        organisation_entry = Organisationmodel.query.filter_by(orgaid=organisation_id).first()
        db.session.commit()
        result = jsonify( category="Success.", 
                message=f"Organisation with ID {organisation_id} successfully modified.",
                dataobj=organisation_entry.to_dict(only=(
                    'orgaid',
                    'name'
                ))) if org else (jsonify (category="Error",
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


@Organisation.route('/own/', methods=['GET'])
@auth_required([Config.ADMIN_ID, Config.SUPERADMIN_ID, Config.TEACHER_ID])
def get_own_role():
    return jsonify(Organisation= get_jwt()["organisation"])

