from flask import Flask, request
from pymongo import MongoClient
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask(__name__)
client = MongoClient("mongodb:27017")
db = client.server
songs = db.songs

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="85d5a82cec1541b8b1dea6b035b097a8", 
                                                           client_secret="9c6945e57e6647dd9874ac74010a4294"))

@app.route('/', methods=['POST'])
def test():
    data = request.get_json(force=True)
    track = sp.track(track_id=data.get('id'))
    return track

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9090, debug=True)