from flask import Blueprint, jsonify, request
from app import db
from models.organisation import Organisation as Organisationmodel
from models.submission import Submission as Submissionmodel
from models.hackathon import Hackathon as Hackathonmodel
from utils.user_roles import auth_required, Config
from sqlalchemy.exc import InvalidRequestError, IntegrityError
from flask_jwt_extended import get_jwt

Submission = Blueprint('submission', __name__)


""" @Submission.route('/', methods=["POST"])
@auth_required([Config.SUPERADMIN_ID])
def add_organisation():

    org = request.get_json()
    entry = Organisationmodel(**org)
    db.session.add(entry)
    db.session.commit()

    return jsonify(category="Success.", message=f"Organisation added.")
 """

@Submission.route('/<hackathon_id>/', methods=["GET"])
@auth_required([Config.TEACHER_ID, Config.ADMIN_ID])
def get_submissions(hackathon_id):
    result = jsonify(category="Error", message=f"No Access rights.")
    organisation = get_jwt()["organisation"]
    valid = Hackathonmodel.query.filter_by(hackathonid = hackathon_id, organisationid=organisation).first()
    if valid:
        getAll = Submissionmodel.query.filter_by(hackathonid=hackathon_id).all()    
        result = jsonify([submission.to_dict(only=('subid', 'description')) for submission in getAll])
    return result

@Submission.route('/<submission_id>/', methods=["PATCH"])
@auth_required([Config.TEACHER_ID, Config.ADMIN_ID])
def change_submission(submission_id):
    result = (jsonify(category="Error", message=f"No Access rights."),403)
    organisation = get_jwt()["organisation"]
    data = request.get_json()

    try:
        sub = Submissionmodel.query.filter_by(subid=submission_id).first()        
        valid = Hackathonmodel.query.filter_by(hackathonid = sub.hackathonid, organisationid=organisation).first()        
        if valid: 
            sub = Submissionmodel.query.filter_by(subid=submission_id).update(data)
            db.session.commit()
            result = jsonify( category="Success.", 
                message=f"Submission with ID {submission_id} successfully modified.") if sub else (jsonify (category="Error",
                message=f"No Submission with ID: {submission_id}"))
    except:
        db.session.rollback()
        result = jsonify(category="Error", message=f"Error while editing Submission.")

    return result


@Submission.route('/<submission_id>/', methods=["DELETE"])
@auth_required([Config.TEACHER_ID, Config.ADMIN_ID])
def delete_organisation(submission_id):
    result = (jsonify(category="Error", message=f"No Access rights."),403)
    organisation = get_jwt()["organisation"]
    try:
        sub = Submissionmodel.query.filter_by(subid=submission_id).first()
        valid = Hackathonmodel.query.filter_by(hackathonid = sub.hackathonid, organisationid=organisation).first()
        if valid:
            Submissionmodel.query.filter_by(subid=submission_id).delete()
            db.session.commit()
            result = jsonify( category="Success.", 
                    message=f"Submission with ID {submission_id} successfully deleted.")
    except:
        result = (jsonify(category="Error", 
                    message=f"No Submission with ID: {submission_id}"), 409)
    
    return  result
