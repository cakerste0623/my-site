from http import HTTPStatus
import json
import os
from flask import Flask, jsonify, request
import hashlib
import datetime
from pymongo import MongoClient, DESCENDING
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask(__name__)
# TODO change these credentials (obviously) and use env variables instead
client = MongoClient("mongodb://collin:password@mongodb:27017/?authSource=server")
db = client.server
songs = db.songs

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=os.environ['CLIENT_ID'], 
                                                           client_secret=os.environ['CLIENT_SECRET']))

def createId(data):
    hash = hashlib.md5()
    encoded = json.dumps(data, sort_keys=True).encode()
    hash.update(encoded)
    return str(hash.hexdigest())

def parseDataAndPush(track):
    track_data = {}
    track_data['name'] = track.get('name')
    track_data['artist'] = track.get('artists')[0].get('name')
    track_data['album'] = track.get('album').get('name')
    track_data['releaseDate'] = track.get('album').get('release_date')
    track_data['coverImage'] = track.get('album').get('images')[0].get('url')
    track_data['createTimestamp'] = str(datetime.datetime.now())
    track_data['_id'] = createId(track_data)

    try:
        songs.insert_one(track_data)
    except:
        return {"msg": "Error saving track to database"}, HTTPStatus.BAD_REQUEST
    return track_data

@app.route('/song', methods=['POST', 'GET'])
def post_and_get_song():
    if request.method == 'POST':
        data = request.get_json(force=True)

        try:
            track = sp.track(track_id=data.get('id'))
        except:
            return jsonify({"msg": "Could not find track with the given id"}), HTTPStatus.NOT_FOUND
        t = parseDataAndPush(track)
        return jsonify(t), HTTPStatus.OK
    else:
        latest_song = songs.find_one(sort=[('createTimestamp', DESCENDING)])
        return jsonify(latest_song), HTTPStatus.OK

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9090, debug=True)
