# Create an extra function to check tokens for rightful access to data
# and create an encoder for our JSON content
# If a user doesn't have access to the data, they will be denied access

from functools import wraps
import secrets
from flask import request, jsonify, json
import decimal

from models import User

# Function to require token to make sure users are doing what they're supposed to
def token_required(our_flask_function):
    @wraps(our_flask_function)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            # will have token number to check that's at index 1 from dictionary headers
            # headers is key, 'x-access-token' is value
            token = request.headers['x-access-token'].split(' ')[1]
        if not token:
            return jsonify({'message': 'Token is missing.'}), 401

        try:
            # go to User class, ask it for something, filter it by token, bring back the first of it
            current_user_token = User.query.filter_by(token=token).first()
            print(token)
            print(current_user_token)
        except:
            owner = User.query.filter_by(token=token).first()

            if token != owner.token and secrets.compare_digest(token, owner.token):
                return jsonify({'message': 'Token is invalid'})
        return our_flask_function(current_user_token, *args, **kwargs)
    return decorated

# This checks the instances of json are decimals, and then changes them into string that we can use later
class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return str(obj)
        return super(JSONEncoder,self).default(obj)