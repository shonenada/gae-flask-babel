from flask import Blueprint


home_app = Blueprint('home', __name__)


@home_app.route('/')
def index():
    return 'Halo~'
