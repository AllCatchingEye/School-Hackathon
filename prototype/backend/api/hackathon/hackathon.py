from flask import Blueprint, jsonify, request
from app import db
from models.hackathon import Hackathon as Hackathonmodel
from flask_jwt_extended import get_jwt
from utils.user_roles import auth_required, Config
from flask_expects_json import expects_json
from sqlalchemy.exc import IntegrityError
from urllib import parse

Hackathon = Blueprint('hackathon', __name__)

    
@Hackathon.route('/', methods=["GET"])
@auth_required([Config.ADMIN_ID, Config.TEACHER_ID])
def get_hackathons():
    organisation = get_jwt()["organisation"]
    hackathons = Hackathonmodel.query.filter_by(organisationid=organisation).all()
    return jsonify([hackathon.to_dict(only=(
                                'title',
                                'hackathonid',     
                                'slug',                       
                                'description')) for hackathon in hackathons])


@Hackathon.route('/<hackathon_id>/', methods=["GET"])
@auth_required([Config.ADMIN_ID, Config.TEACHER_ID])
def get_hackathon(hackathon_id):
    organisation = get_jwt()["organisation"]
    hackathon = Hackathonmodel.query.filter_by(organisationid=organisation,hackathonid=hackathon_id).first()
    return jsonify(hackathon.to_dict(only=(
                                    'title',    
                                    'hackathonid', 
                                    'slug',
                                    'description'))) if hackathon else jsonify(category="Error", 
                                    message=f"No Hackathon with id: {hackathon_id}")



@Hackathon.route('/<hackathon_id>/', methods=["DELETE"])
@auth_required([Config.ADMIN_ID])
def delete_hackathon(hackathon_id):        
    organisation = get_jwt()["organisation"]    
    response = Hackathonmodel.query.filter_by(organisationid=organisation, hackathonid=hackathon_id).first()
    db.session.delete(response)
    db.session.commit()
    return jsonify( category="Success", 
                    message=f"Hackathon deleted.") if response else jsonify(category="Error", 
                          message=f"No Hackathon with id: {hackathon_id}")


hackathon_schema = {
    'type': 'object',
    'properties': {
        'title': {'type': 'string'},
        'description': {'type': 'string'},
        'slug': {'type': 'string'}
    },
    'required': ['description', 'title', 'slug']
}

@Hackathon.route('/', methods=["POST"])
@auth_required([Config.ADMIN_ID])
@expects_json(hackathon_schema) 
def create_hackathon():
    organisation = get_jwt()["organisation"]
    data = request.get_json()
    hackathon = Hackathonmodel(**data, organisationid=organisation)
    db.session.add(hackathon)
    result = (jsonify(
                    category="Error",
                    message=f"Error while adding hackathon"), 409)
    try:
        db.session.commit()
        result = (jsonify(
                    category="Success",
                    message=f"Added Hackathon {hackathon.title} with url: {hackathon.slug}",
                    dataobj=hackathon.to_dict(only=(
                                'title', 
                                'hackathonid', 
                                'slug', 
                                'description'))), 201)
    except IntegrityError as e:
        result = (jsonify(
                    category="Error",
                    message=f"Hackathon with slug {hackathon.slug} already exists"), 409)
        db.session.rollback()
    except:
        db.session.rollback()

    return result



@Hackathon.route('/<hackathon_id>/', methods=["PATCH"])
@auth_required([Config.ADMIN_ID])
def edit_hackathon(hackathon_id):        
    data_request = request.get_json()
    organisation = get_jwt()["organisation"]    
    data_request["slug"] = parse.quote_plus(data_request["slug"])
    result = (jsonify(
                category="Error",
                message=f"Error while editing hackathon"), 409) 
    try:
        hackathon = Hackathonmodel.query.filter_by(organisationid=organisation, hackathonid=hackathon_id).update(data_request)
        hackathon_entry = Hackathonmodel.query.filter_by(organisationid=organisation, hackathonid=hackathon_id).first()
        db.session.commit()
        result = jsonify( category="Success", 
                    message=f"Hackathon edited",
                    dataobj=hackathon_entry.to_dict(only=(
                                'title', 
                                'hackathonid', 
                                'slug', 
                                'description'))) if hackathon else jsonify(category="Error", 
                            message=f"No Hackathon with id: {hackathon_id}")
    except IntegrityError as e:
        result = (jsonify(
                    category="Error",
                    message=f"Hackathon with slug {data_request['slug']} already exists"), 409)
        db.session.rollback()
    except:
        db.session.rollback()

    return result
