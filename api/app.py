from enum import unique
import os
from flask import Flask, request, jsonify
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
        self.username = username
        self.password = password

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    user = User.query.filter_by(username=username).first()
    
    if user:
        if bcrypt.checkpw(bytes(password, 'utf-8'), user.password):
            jsonify({"success": "user access granted"})
        else:
            print("Password does not match")
            jsonify({"error": "Passwords do not match"})
    else:
        return jsonify({"error": "This user does not exist"})



@app.route("/register", methods=["POST"])
def register():

    data = request.get_json()
    username = data['username']
    password = data['password']

    print(User.query.filter_by(username=username).first())

    if User.query.filter_by(username=username).first():
        jsonify({"error": "Username already exists"})
        
    else:
        hashed_password = bcrypt.hashpw(bytes(password, 'utf-8'),bcrypt.gensalt())
        
        user = User(username, hashed_password)

        db.session.add(user)
        db.session.commit()

    return ""
