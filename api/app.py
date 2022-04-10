
import os
import bcrypt
import requests

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_jwt_extended import create_access_token
from flask_jwt_extended import set_access_cookies
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import get_jwt
from flask_jwt_extended import unset_jwt_cookies
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

from datetime import datetime
from datetime import timedelta
from datetime import timezone

app = Flask(__name__)
CORS(app, supports_credentials=True) #supports_credentials allows cookies or authenticated requests to be made cross origins

                           
SECRET_KEY = os.getenv("SECRET_KEY")
app.config['SECRET_KEY'] = SECRET_KEY

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

app.config["JWT_SECRET_KEY"] = "super-secret" 
app.config["JWT_COOKIE_SECURE"] = False
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config['JWT_CSRF_IN_COOKIES'] = True


db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    movies = db.relationship('Movie', backref='user', lazy=True)
    swiped = db.relationship('Swiped', backref='user', lazy=True)
    genres = db.relationship('Genres', backref='user', lazy=True)

    def __init__ (self, username, password):
        self.username = username
        self.password = password

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie = db.Column(db.PickleType, nullable=False)
    movie_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, movie, movie_id, user_id):
        self.movie = movie
        self.movie_id = movie_id
        self.user_id = user_id

class Swiped(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, movie_id, user_id):
        self.movie_id = movie_id
        self.user_id = user_id

class Genres(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genres = db.Column(db.PickleType, nullable=False)
    page_number = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, genres, page_number, user_id):
        self.genres = genres
        self.page_number = page_number
        self.user_id = user_id

@app.after_request
def check_JWT_expiration(response):
    print('after_request fired')
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            set_access_cookies(response, access_token)
            print("token refreshed")
        return response
    except (RuntimeError, KeyError):
        return response

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    user = User.query.filter_by(username=username).first()
    
    if user:
        if bcrypt.checkpw(bytes(password, 'utf-8'), user.password):
            access_token = create_access_token(identity=username)
            response = jsonify({"success": "user access granted"})
            set_access_cookies(response, access_token)
            return response
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


@app.route("/logout", methods=["POST"])
def logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response

@app.route('/movie_list', methods=["POST"])
@jwt_required()
def movies():
    key = os.getenv('MOVIE_KEY')
    data = request.get_json()
    genres = data["genres"]
    genre_id_list = []

    for genre_obj in genres:
        genre_id_list.append(str(genre_obj['id']))

    genre_query_string = ",".join(genre_id_list)
    response = requests.get(f'https://api.themoviedb.org/4/discover/movie?with_genres={genre_query_string}&api_key={key}&language=en-US')
    return jsonify({"data": response.json()})

@app.route("/save_movie", methods=["POST"])
@jwt_required()
def save_movie():
    movie_data = request.get_json()
    username = get_jwt_identity()
    user_obj = User.query.filter_by(username=username).first()
    movie = Movie(movie_data, movie_data['id'], user_obj.id)
    db.session.add(movie)
    db.session.commit()
    return jsonify({"msg": "movie saved"})

@app.route("/delete_movie", methods=["DELETE"])
@jwt_required()
def delete_movie():
    movie_id = request.get_json()
    username = get_jwt_identity()
    user_obj = User.query.filter_by(username=username).first()

    matched_movie = Movie.query.filter_by(user_id=user_obj.id, movie_id=movie_id).first()
    db.session.delete(matched_movie)
    db.session.commit()
    return jsonify({"resp": "you hit delete route"})

@app.route("/user_movie_list")
@jwt_required()
def get_movies():
    username = get_jwt_identity()
    user_obj = User.query.filter_by(username=username).first()

    movies = []
    for movie in user_obj.movies:
        print(movie.movie)
        movies.append(movie.movie)
    return jsonify(movies)

@app.route("/swiped", methods=["GET", "POST"])
@jwt_required()
def swiped():
    if request.method == "GET":
        username = get_jwt_identity()
        user_obj = User.query.filter_by(username=username).first()

        swiped_ids = []
        for id in user_obj.swiped:
            swiped_ids.append(id.movie_id)
        
        return jsonify(swiped_ids)

    if request.method == "POST":
        movie_obj = request.get_json()

        username = get_jwt_identity()
        user_obj = User.query.filter_by(username=username).first()

        swiped = Swiped(movie_obj['id'], user_obj.id)
        db.session.add(swiped)
        db.session.commit()

    return jsonify({'msg':''})

