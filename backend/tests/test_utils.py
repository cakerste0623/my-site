from utils import *

def test_one_artist():
  data = [
    {
      "external_urls": {
        "spotify": "https://open.spotify.com/artist/5INjqkS1o8h1imAzPqGZBb"
      },
      "href": "https://api.spotify.com/v1/artists/5INjqkS1o8h1imAzPqGZBb",
      "id": "5INjqkS1o8h1imAzPqGZBb",
      "name": "Tame Impala",
      "type": "artist",
      "uri": "spotify:artist:5INjqkS1o8h1imAzPqGZBb"
    }
  ]

  artist = getArtists(data)
  assert len(artist) == 1
  assert artist[0] == "Tame Impala"

def test_multiple_artists():
  data = [
    {
      "external_urls": {
        "spotify": "https://open.spotify.com/artist/1hLiboQ98IQWhpKeP9vRFw"
      },
      "href": "https://api.spotify.com/v1/artists/1hLiboQ98IQWhpKeP9vRFw",
      "id": "1hLiboQ98IQWhpKeP9vRFw",
      "name": "boygenius",
      "type": "artist",
      "uri": "spotify:artist:1hLiboQ98IQWhpKeP9vRFw"
    },
    {
      "external_urls": {
        "spotify": "https://open.spotify.com/artist/12zbUHbPHL5DGuJtiUfsip"
      },
      "href": "https://api.spotify.com/v1/artists/12zbUHbPHL5DGuJtiUfsip",
      "id": "12zbUHbPHL5DGuJtiUfsip",
      "name": "Julien Baker",
      "type": "artist",
      "uri": "spotify:artist:12zbUHbPHL5DGuJtiUfsip"
    },
    {
      "external_urls": {
        "spotify": "https://open.spotify.com/artist/1r1uxoy19fzMxunt3ONAkG"
      },
      "href": "https://api.spotify.com/v1/artists/1r1uxoy19fzMxunt3ONAkG",
      "id": "1r1uxoy19fzMxunt3ONAkG",
      "name": "Phoebe Bridgers",
      "type": "artist",
      "uri": "spotify:artist:1r1uxoy19fzMxunt3ONAkG"
    },
    {
      "external_urls": {
        "spotify": "https://open.spotify.com/artist/07D1Bjaof0NFlU32KXiqUP"
      },
      "href": "https://api.spotify.com/v1/artists/07D1Bjaof0NFlU32KXiqUP",
      "id": "07D1Bjaof0NFlU32KXiqUP",
      "name": "Lucy Dacus",
      "type": "artist",
      "uri": "spotify:artist:07D1Bjaof0NFlU32KXiqUP"
    }
  ]
  artists = getArtists(data)
  assert len(artists) == 4
  assert "boygenius" in artists
  assert "Julien Baker" in artists
  assert "Phoebe Bridgers" in artists
  assert "Lucy Dacus" in artists

def test_get_genre():
  data = "https://open.spotify.com/artist/2x9SpqnPi8rlE9pjHBwmSC"
  genre = getGenre(data)
  assert genre == "Art Punk"

def test_get_genre_no_genre():
  data = "https://open.spotify.com/artist/3dBOwPj9GaClkPMJXIruFP"
  genre = getGenre(data)
  assert genre == "N/A"

def test_get_track_by_id():
  data = "2ciMJGCDW70hqq18Vgui68"
  track = getTrackById(data)
  assert track.get('name') == "Who'll Stop The Rain"
  assert len(track.get('artists'))
  assert track.get('artists')[0].get('name') == "Creedence Clearwater Revival"

def test_get_track_by_id_invalid():
  data = "INVALID_TRACK_ID"
  track = getTrackById(data)
  assert track.get('msg') == "Could not find track with the given id"

def test_get_track_by_song_artist():
  song = "Not My Baby"
  artist = "Alvvays"
  track = getTrackBySongAndArtist(song, artist)
  assert track.get('name') == song
  assert len(track.get('artists')) == 1
  assert track.get('artists')[0].get('name') == artist

def test_get_track_by_song_artist_imprecise():
  song = "Your mirror ill be"
  artist = "the velvets"
  track = getTrackBySongAndArtist(song, artist)
  assert track.get('name') == "I'll Be Your Mirror"
  assert len(track.get('artists')) == 2
  assert track.get('artists')[0].get('name') == "The Velvet Underground"
  assert track.get('artists')[1].get('name') == "Nico"

def test_parse_data():
  song = "The Divine Chord"
  artist = "The Avalanches"
  track = getTrackBySongAndArtist(song, artist)
  parsed_track = parseData(track)
  assert parsed_track.get('name') == "The Divine Chord"
  assert len(parsed_track.get('artists')) == 3
  assert parsed_track.get('artists')[0] == "The Avalanches"
  assert parsed_track.get('artists')[1] == "MGMT"
  assert parsed_track.get('artists')[2] == "Johnny Marr"
  assert parsed_track.get('album') == "We Will Always Love You"
  assert parsed_track.get('releaseYear') == "2020"
  assert parsed_track.get('_id') is not None
