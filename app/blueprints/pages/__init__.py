from flask import Blueprint

pages = Blueprint('pages', __name__, template_folder='templates')


@pages.route('/')
def index():
    return '<h1>Hello world!</h1>'
