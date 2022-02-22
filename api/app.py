from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/login")
def login():
    return {"test": "TEST"}


@app.route("/register")
def register():
    return {"test": "TEST"}

app.run(debug=True)