# importing jsonify makes it so we can take our data and put it into json format
# so we can peruse the data with JS and Python
from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Contact, contact_schema, contacts_schema

# every time we run an api we need /api before the slug
api = Blueprint('api', __name__, url_prefix='/api')