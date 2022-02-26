from enum import unique
import os
from flask import Flask, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import bcrypt

app = Flask(__name__)
CORS(app)                                   


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# SECRET_KEY = os.environ.get("SECRET_KEY")

db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'secret_key'

print(os.environ['HOME'])

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

    def __init__ (self, username, password):
        username = self.username
        password = self.password

@app.route("/login")
def login():
    return {"test": "TEST"}


@app.route("/register", methods=["POST"])
def register():

    data = request.get_json()
    print(data)
    username = data['username']
    password = data['password']

    if User.query.filter_by(username=username).first():
        print("username already exists")
    else:
        hashed_password = bcrypt.hashpw(password,bcrypt.gensalt())


    return {"test": "TEST"}

