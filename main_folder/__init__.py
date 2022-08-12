# This file is the first thing our app runs
# It's the brain of our app

from flask import Flask
# importing the Config class from config file
from config import Config
# We created the value site on routes.py (line 9), which references the template_folder='site_templates'
from .site.routes import site
# This comes from the auth value in the authentication folder
from .authentication.routes import auth
# Importing from routes in api folder
from .api.routes import api

# These all need to be imported because we used SQLAlchemy for our logic in config and models
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db as root_db, login_manager, ma
# helps prevents cross site request forgery (hackers)
from flask_cors import CORS
from helpers import JSONEncoder


app = Flask(__name__)
# instaniating the CORS
CORS(app)
# this registers the blueprint to the app (app.register_blueprint) and tells us where it's registered to (site)
app.register_blueprint(site)
app.register_blueprint(auth)
app.register_blueprint(api)
# will help us peruse the data in json format
app.json_encoder = JSONEncoder
# this will configure the app, database will connect, and the .env will be connected
app.config.from_object(Config)
# These initiate the database with the app and run the login manager.
# They also get our app ready to upload and modify the database tables using Migrate
root_db.init_app(app)
login_manager.init_app(app)
ma.init_app(app)
migrate = Migrate(app, root_db)