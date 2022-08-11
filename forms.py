# will import specific tools that will make sure users are giving us proper info
# pulling in the following modules to help with the UserLoginForm class below.
from flask_wtf import FlaskForm
# stringfield makes sure the input is a string, password field hides the input as it's entered,
# and submitfield ties its submit-time data with the other FlaskForm fields.
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

#  Will get pulled into routes.py
class UserLoginForm(FlaskForm):
    # creates an email variable that makes sure it's a string input in email format
    # DataRequired() and Email() run something like regex on the forms to make sure it's the proper data type
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit_button = SubmitField()