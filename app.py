from flask import Flask
from flask import render_template
from flask import Flask, Response, redirect, url_for, request, session, abort
from flask_login import LoginManager, UserMixin, \
                                login_required, login_user, logout_user
from flask.ext.login import login_user
from mockdbhelper import MockDBHelper as DBHelper
from user import User
from flask import redirect
from flask import url_for
from flask import request

DB = DBHelper()

app = Flask(__name__)

app.secret_key = 'tPXJY3X37Qybz4QykV+hOyUxVQeEXf1Ao2C8upz+fGQXKsM'

login_manager = LoginManager(app)


@app.route("/")
def home():
   return render_template("home.html")

@app.route("/account")
@login_required
def account():
   return "You are logged in"

@app.route("/login", methods=["POST"])
def login():
   email = request.form.get("email")
   password = request.form.get("password")
   user_password = DB.get_user(email)
   if user_password and user_password == password:
      user = User(email)
      login_user(user)
      return redirect(url_for('account'))
   return home()

if __name__ == '__main__':
    app.run(port=5000, debug=True)