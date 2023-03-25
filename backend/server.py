from http import HTTPStatus
import os
from flask import Flask, jsonify, request
import datetime
import jwt
from pymongo import MongoClient, DESCENDING
from werkzeug.security import check_password_hash
from utils import *

# Time that the JWT is valid for (in seconds)
exp_time = 300

app = Flask(__name__)
client = MongoClient("mongodb", username=os.environ['MONGO_USERNAME'], password=os.environ['MONGO_PWD'], authSource="server")
db = client.server
songs = db.songs

@app.route('/song', methods=['POST', 'GET'])
def post_and_get_song():
    if request.method == 'POST':
        token = request.headers.get('Authorization')
        if not token:
            return {"msg": "No token given"}, HTTPStatus.UNAUTHORIZED

        try:
            decoded_token = jwt.decode(token, os.environ['JWT_KEY'], algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return {"msg": "Expired Token"}, HTTPStatus.UNAUTHORIZED

        if decoded_token.get('user') is None:
            return {"msg": "Invalid token"}, HTTPStatus.UNAUTHORIZED

        data = request.get_json(force=True)

        if data.get('id') is not None:
            track = getTrackById(data.get('id'))
        elif data.get('song') is not None and data.get('artist') is not None:
            track = getTrackBySongAndArtist(data.get('song'), data.get('artist'))
        else:
            return {"msg": "Invalid request"}, HTTPStatus.BAD_REQUEST

        if track.get('msg') is not None:
            return jsonify(track), HTTPStatus.BAD_REQUEST

        t = parseData(track)
        try:
            songs.insert_one(t)
        except:
            return t, HTTPStatus.BAD_REQUEST
        return t, HTTPStatus.OK
    elif request.method == 'GET':
        latest_song = songs.find_one(sort=[('createTimestamp', DESCENDING)])
        return jsonify(latest_song), HTTPStatus.OK
    else:
        return {"msg": "Method not supported"}, HTTPStatus.METHOD_NOT_ALLOWED

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json(force=True)
    users = db.users
    user = users.find_one({"username": data.get('username')})
    if user is None or not check_password_hash(user.get('password'), data.get('password')):
        return {"msg": "Unable to log in"}, HTTPStatus.UNAUTHORIZED
    
    token = jwt.encode({"user": user.get('username'), "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=exp_time)}, os.environ['JWT_KEY'], algorithm="HS256")
    return jsonify({"token": token}), HTTPStatus.OK

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9090, debug=True)
