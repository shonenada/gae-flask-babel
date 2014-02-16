from flask import Blueprint, render_template
from flask.ext.babel import gettext as _


home_app = Blueprint('home', __name__, template_folder='../templates')


@home_app.route('/')
def index():
    return render_template('index.html')
