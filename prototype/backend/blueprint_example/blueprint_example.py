from flask import Blueprint

blueprint_example = Blueprint('blueprint_example', __name__,
                        template_folder='templates')

@blueprint_example.route('/')
def show():
    return "Hello World"