from enum import unique
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import bcrypt
import requests
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = Flask(__name__)
CORS(app)
                           
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
SECRET_KEY = os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = SECRET_KEY
db = SQLAlchemy(app)

jwt = JWTManager(app)

class User(db.Model):
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
            access_token = create_access_token(identity=username);
            return jsonify({"success": "user access granted", "token": access_token})
        else:
            return jsonify({"error": {"password" :"Passwords do not match"}})
    else:
        return jsonify({"error": {"username":"This username does not exist"}})


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already exists"})
        
    else:
        hashed_password = bcrypt.hashpw(bytes(password, 'utf-8'),bcrypt.gensalt())
        user = User(username, hashed_password)

        db.session.add(user)
        db.session.commit()
        return jsonify({"success": "User registered"})


@app.route('/logout', methods=["GET", "POST"])
def logout():
    pass

@app.route('/movies', methods=["POST"])
def books():
    data = request.get_json()
    genre_id = data['genre_id']
    key = os.getenv('MOVIE_KEY')
    response = requests.get(f'https://api.themoviedb.org/4/discover/movie?with_genres={genre_id}&api_key={key}&language=en-US')
    return jsonify({"data": response.json()})

