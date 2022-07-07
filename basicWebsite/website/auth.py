from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

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
        first_name = request.form.get("first_name")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if len(email) < 4:
            flash("Email must be greater than 4 characters.", category="error")
        elif len(first_name) < 2:
            flash("First name must be greater than 1 character", category="error")
        elif password1 != password2:
            flash("Password must match", category="error")
        elif len(password1) < 4:
            flash("Password must be greater than 7 characters", category="error")
        else:
            # Add User to Database
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method="sha256"))
            db.session.add(new_user)
            db.session.commit()

            flash("Account created", category="Success")

            return redirect(url_for("views.home"))

    return render_template('signUp.html')

