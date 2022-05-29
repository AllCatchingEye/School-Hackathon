# Helper functions for the different user types.
# Roles:
# Superadmin -> wirfuerschule Team              
# Admin      -> Admin for a specific school     
# Teacher    -> Teacher of a specific school 
# User       -> Pupil of a specific school

from unicodedata import category
from flask import  jsonify
from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt

class Config(object):
    SUPERADMIN_ID = 420
    ADMIN_ID = 29
    TEACHER = 12
    USER = 1

# Here is a custom decorator that verifies the JWT is present in the request,
# as well as insuring that the JWT has a claim indicating that this user has one of the role 
# given in accepted_roles
def auth_required(accepted_roles):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            print(claims)
            return fn(*args, **kwargs) if claims["role"] in accepted_roles else jsonify(
                category= "Error"
                message=f'No {claims["role"]}!'), 403           
        return decorator
    return wrapper
