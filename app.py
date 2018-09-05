from flask import Flask
from flask import render_template
from flask import Flask, Response, redirect, url_for, request, session, abort
from flask_login import LoginManager, UserMixin, \
                                login_required, login_user, logout_user

app = Flask(__name__)
login_manager = LoginManager(app)

@app.route("/")
def home():
   return render_template("home.html")

@app.route("/account")
@login_required
def account():
   return "You are logged in"

if __name__ == '__main__':
    app.run(port=5000, debug=True)