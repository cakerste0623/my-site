# Usage: ./loginAndAddSong.sh {song_id}
TOKEN=`curl -s -X POST localhost/api/login -d "{\"username\": \"$DB_USERNAME\", \"password\": \"$DB_PWD\"}" | jq '.token' | sed -e 's/^"//' -e 's/"$//'`
curl -X POST localhost/api/song -d "{\"id\": \"$1\"}" -H "Authorization: $TOKEN"