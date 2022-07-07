from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=["GET", "POST"])
def login():
    data = request.form
    print(data)
    return render_template('login.html', boolean=True)

@auth.route('/logout')
def logout():
    return render_template('logout.html')

@auth.route('/sign-up', methods=["GET", "POST"])
def signUp():
    if request.method == "POST":
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if len(email) < 4:
            flash("Email must be greater than 4 characters.", category="error")
        elif len(firstName) < 2:
            flash("First name must be greater than 1 character", category="error")
        elif password1 != password2:
            flash("Password must match", category="error")
        elif len(password1) < 7:
            flash("Password must be greater than 7 characters", category="error")
        else:
            # Add User to Database
            flash("Account created", category="Success")
    return render_template('signUp.html')

