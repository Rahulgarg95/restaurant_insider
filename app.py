from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
   return "Its going to be fun"

if __name__ == '__main__':
    app.run(port=5000, debug=True)