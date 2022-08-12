# Blueprint is a class that makes a blueprint and allows us to access the file structure around the templates
# render_template is the function that runs html
from flask import Blueprint, render_template

# WHERE IS THIS COMING FROM? .... WHERE THE CODE BELOW WILL SEARCH
# 'site' references the folder site
# __name__ references the routes.py __init__ 
# template_folder = 'site_templates references the folder within site.. site_templates
site = Blueprint('site', __name__, template_folder='site_templates')

# this is the slug and destination of where the site will take us  (the route we take for site (as established above))
@site.route('/')
# this is the function that will run to bring back the html we choose
def home():
    return render_template('index.html')

@site.route('/profile')
def profile():
    return render_template('profile.html')