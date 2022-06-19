from flask import Blueprint, jsonify,request, render_template
from models.user import User
from app import db,mail
from sqlalchemy.exc import IntegrityError
from flask_expects_json import expects_json
from models.organisation import Organisation
from models.roles import Roles
from utils.user_roles import auth_required, Config
from flask_jwt_extended import get_jwt
import secrets
from flask_mail import Message
from email.utils import formataddr
from smtplib import SMTP_SSL, SMTPException
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SENDER = 'no-reply@wirfuerschule.lio.codes'
SENDERNAME = 'WirfürSchule'
USERNAME_SMTP = "AKIAWKJEZSOKD57VRAPE"
PASSWORD_SMTP = "BM/hxGfDHxke8L0DhERHnMSmNhOYe8VNvXsRLWiQBdqT"
HOST = "email-smtp.eu-central-1.amazonaws.com"
PORT = 465
SUBJECT = 'Registrierung'


Register = Blueprint('register', __name__,template_folder='mails')
register_schema = {
    'type': 'object',
    'properties': {
        'email': {'type': 'string'},
        'name': {'type': 'string'},
        'firstname': {'type': 'string'},
        'role': {'type': 'integer'},
        'organisation': {'type': 'integer'}
    },
    'required': ['email', 'name', 'firstname', 'role', 'organisation']
}

def sendRegistration(name, password, mailAddress):

    RECIPIENT = mailAddress
    BODY_TEXT = ("Hallo {name}\r\n"
                 "Dein Password ist: {password} ")

    # The HTML body of the email.
    BODY_HTML = render_template('set-password.html', username = name, password=password)

    msg = MIMEMultipart('alternative')
    msg['Subject'] = SUBJECT
    msg['From'] = formataddr((SENDERNAME, SENDER))
    msg['To'] = RECIPIENT

    part1 = MIMEText(BODY_TEXT, 'plain')
    part2 = MIMEText(BODY_HTML, 'html')

    msg.attach(part1)
    msg.attach(part2)

    # Try to send the message.
    try:
        with SMTP_SSL(HOST, PORT) as server:
            server.login(USERNAME_SMTP, PASSWORD_SMTP)
            server.sendmail(SENDER, RECIPIENT, msg.as_string())
            server.close()
            print("Email sent!")

    except SMTPException as e:
        print("Error: ", e)



@Register.route('/', methods=['POST'])
@auth_required([Config.ADMIN_ID, Config.SUPERADMIN_ID])
@expects_json(register_schema) # Compares request schema with expected schema 
def create():
    valid = False
    result = (jsonify(category = "Error", message="Hmm there is something wrong"), 409)
    organisation = get_jwt()["organisation"]    

    data_request = request.get_json()
    requested_role = data_request["role"]
    if get_jwt()["role"] == Config.ADMIN_ID:
        if requested_role in [Config.ADMIN_ID, Config.TEACHER_ID]:
            valid = True
    elif get_jwt()["role"] == Config.SUPERADMIN_ID:
        if requested_role in [Config.ADMIN_ID, Config.SUPERADMIN_ID]:
            valid = True
    if valid:

        # Create User with new password
        user_data = request.get_json()
        user_password = secrets.token_urlsafe(5)
        if get_jwt()["role"] == Config.ADMIN_ID:
                user_data['organisation'] = organisation

        user = User(**user_data, password=user_password)    

        # Create E-Mail

        db.session.add(user)            
        try:
            db.session.commit()
                
            result = (jsonify(
                    category="Success",
                    message=f"User: {user.name} created",
                    dataobj=user.to_dict()), 201)
            # Send E-Mail
            sendRegistration(user.name, user_password, user.email)
        except IntegrityError as er:
            db.session.rollback()
            result = (jsonify(
                    category="Error",
                    message=f"Hmm there is something wrong. Maybe E-mail already exists. "), 409)
        except Exception as e:
            print(e)
    return result

# # Testing method to add something to database
# @Register.route('/add/', methods=['GET'])
# def add_to_db():
#     """
#         Add to DB
#     """
#     """
#     role = Roles(420, "Superadmin", "Total Access")
#     db.session.add(role)
#     db.session.commit()
#     role = Roles(29, "Admin", "Normal Access")
#     db.session.add(role)
#     db.session.commit()
#     role = Roles(12, "Teacher", "Teacher Access")
#     db.session.add(role)
#     db.session.commit()
#     role = Roles(1, "User", "User Access")
#     db.session.add(role)
#     db.session.commit()

#     organisation = Organisation("MUCDAI")
#     db.session.add(organisation)
#     db.session.commit()
#     """

#     organisation = User("muc@dealer.com", "Mucdai","Mucdai", "muc", 420, 1)
#     db.session.add(organisation)
#     db.session.commit()

#     return str(organisation)