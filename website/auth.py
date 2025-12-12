from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html", boolean = True)

@auth.route('/logout')
def logout():
    return '<p>Logout</p>'

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.method.get('email')
        firstName = request.method.get('firstName')
        password1 = request.method.get('password1')
        password2 = request.method.get('password2')

        if len(email) < 4:
            pass
        elif len(firstName) < 2:
            pass
        elif password1 != password2:
            pass
        elif len(password1) < 7:
            pass
        else:
            # add user to database
            pass
    return render_template("sign_up.html")