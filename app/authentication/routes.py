from forms import UserLoginForm
from models import User, db, check_password_hash
from flask import Blueprint, render_template, request, redirect, url_for, flash

# imports for flask login
from flask_login import login_user, logout_user, LoginManager, current_user, login_required

auth = Blueprint('auth', __name__, template_folder='auth_templates')

# methods are what get sent from the browser for the signup page
@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    # UserLoginForm comes from forms.py
    form = UserLoginForm()

    # tries to use this sign up process
    try:
        # comes from forms validator on submit button
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            print(email, password)

            # comes from User class in models.py and includes the data passed in from forms.py
            user = User(email, password = password)

            # adds user to the database
            db.session.add(user)
            db.session.commit()

            # flash will create a pop-up window
            flash(f'You have successfully created a user account {email}', 'User-created')
            # brings user to a different page than they're on (home page)
            return redirect(url_for('site.home'))

    # allows us to handle bad data from user
    except:
        raise Exception('Invalid form data: Please check your form')
    # pass in so our FlaskForms stuff gets injected into the HTML
    return render_template('sign_up.html', form = form)


@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    form = UserLoginForm()

    try:
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            print(email, password)

            # asks our User class to save the current user's name as variable
            logged_user = User.query.filter(User.email == email).first()
            if logged_user and check_password_hash(logged_user.password, password):
                login_user(logged_user)
                flash('You were successful in your initiation. Congratulations, and welcome to the Jedi Knights', 'auth-success')
                # url for can tell Flask to return the HTML for a certain file without having to call a method.
                return redirect(url_for('site.profile'))
            else:
                flash('You do not have access to this content.', 'auth-failed')
                return redirect(url_for('auth.signin'))
    except:
        raise Exception('Invalid Form Data: Please Check your Form')
    return render_template('sign_in.html', form=form)


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('site.home'))
