from http import HTTPStatus
import json
import os
from string import capwords
from flask import Flask, jsonify, request
import hashlib
import datetime
import jwt
from pymongo import MongoClient, DESCENDING
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from werkzeug.security import check_password_hash

# Time that the JWT is valid for (in seconds)
exp_time = 300

app = Flask(__name__)
client = MongoClient("mongodb", username=os.environ['MONGO_USERNAME'], password=os.environ['MONGO_PWD'], authSource="server")
db = client.server
songs = db.songs

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=os.environ['CLIENT_ID'], 
                                                           client_secret=os.environ['CLIENT_SECRET']))

def createId(data):
    hash = hashlib.md5()
    encoded = json.dumps(data, sort_keys=True).encode()
    hash.update(encoded)
    return str(hash.hexdigest())

def getArtists(artists):
    list_of_artists = []
    for artist in artists:
        list_of_artists.append(artist.get('name'))
    return list_of_artists

def getGenre(artist):
    artist_data = sp.artist(artist)
    return capwords(artist_data.get('genres')[0])

def parseDataAndPush(track):
    track_data = {}
    track_data['name'] = track.get('name')
    track_data['artists'] = getArtists(track.get('artists'))
    track_data['album'] = track.get('album').get('name')
    track_data['genre'] = getGenre(track.get('artists')[0].get('external_urls').get('spotify'))
    track_data['releaseYear'] = track.get('album').get('release_date')[0:4]
    track_data['coverImage'] = track.get('album').get('images')[0].get('url')
    track_data['preview'] = track.get('preview_url')
    track_data['createTimestamp'] = str(datetime.datetime.now())
    track_data['_id'] = createId(track_data)

    try:
        songs.insert_one(track_data)
    except:
        return {"msg": "Error saving track to database"}
    return track_data

def getTrackById(id):
    try:
        track = sp.track(id)
    except:
        return {"msg": "Could not find track with the given id"}
    return track

def getTrackBySongAndArtist(song, artist):
    query = "artist: {a} track: {t}"
    try:
        track = sp.search(q=query.format(a=artist, t=song), type="track", limit=1)
    except:
        return {"msg": "Could not find track with the given track/artist"}
    return track.get('tracks').get('items')[0]

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

        t = parseDataAndPush(track)
        if t.get('msg') is not None:
            return jsonify(t), HTTPStatus.BAD_REQUEST
        else:
            return jsonify(t), HTTPStatus.OK
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
