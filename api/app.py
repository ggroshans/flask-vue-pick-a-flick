from enum import unique
import os
from flask import Flask, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

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


@app.route("/login")
def login():
    return {"test": "TEST"}


@app.route("/register", methods=["POST"])
def register():

    print(request.get_json())
    print(request.get_data())
    return {"test": "TEST"}

