# config allows flask to talk to other pieces (like the browser and CLI)
# import os allows us to interface with the CLI and tell it commands
# most of this will be able to be copied and pasted into new apps (don't really need to know how it all works)
import os 
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config():
    '''
        Set config variables for the flask app
        using Environment variables where available.
        Otherwise create the config variable if not done already.
    '''

# How the app talks to computer
    FLASK_APP = os.getenv('FLASK_APP')
    FLASK_ENV = os.getenv('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY') or "secrets oh secrets"
    
# how the app talks to database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_NOTIFICATIONS = False 