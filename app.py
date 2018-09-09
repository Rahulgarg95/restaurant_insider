from __future__ import print_function
import sys
from flask import Flask
from flask.ext.login import LoginManager, login_required, login_user, logout_user
from flask import render_template, redirect, url_for, request

from mockdbhelper import MockDBHelper as DBHelper
from user import User

DB = DBHelper()

app = Flask(__name__)
app.secret_key = 'eQjBXmwhGYsw2pNshN938WPPWA+JxV+95GIvNGEEVNSLRBjeROx+6Jkne4yFrhdEspat7TK8nMVz\
l1UMmB+PC4SNcFzJ1rKSEUq'
login_manager = LoginManager(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/account")
@login_required
def account():
    return "you are logged in"

@app.route("/login", methods =["POST"])
def login():
    email=request.form.get("email")
    password=request.form.get("password")
    user_password=DB.get_user(email)
    
    if user_password and user_password == password:
        user=User(email)
        login_user(user, remember=True)
        return redirect(url_for('account'))
    return home()

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))

@login_manager.user_loader
def load_user(user_id):
    user_password=DB.get_user(user_id)
    if user_password:
        return User(user_id)

if __name__ == '__main__':
    app.run(port=5000,debug=False)