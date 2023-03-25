import datetime
import json
import hashlib
import os
from string import capwords
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=os.environ['CLIENT_ID'], 
                                                           client_secret=os.environ['CLIENT_SECRET']))

def getArtists(artists):
    list_of_artists = []
    for artist in artists:
        list_of_artists.append(artist.get('name'))
    return list_of_artists

def createId(data):
    hash = hashlib.md5()
    encoded = json.dumps(data, sort_keys=True).encode()
    hash.update(encoded)
    return str(hash.hexdigest())

def getGenre(artist):
    artist_data = sp.artist(artist)
    genres = artist_data.get('genres')
    if not genres:
        return "N/A"
    return capwords(genres[0])

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

def parseData(track):
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
    return track_data
