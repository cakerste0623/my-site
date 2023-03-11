# Usage: ./loginAndAddSong.sh {song_id} OR ./loginAndAddSong.sh {song_name} {artist_name}
TOKEN=`curl -s -X POST localhost/api/login -d "{\"username\": \"$DB_USERNAME\", \"password\": \"$DB_PWD\"}" | jq '.token' | sed -e 's/^"//' -e 's/"$//'`
if [ "$#" -eq 1 ]; then
    curl -X POST localhost/api/song -d "{\"id\": \"$1\"}" -H "Authorization: $TOKEN"
elif [ "$#" -eq 2 ]; then
    curl -X POST localhost/api/song -d "{\"song\": \"$1\", \"artist\": \"$2\"}" -H "Authorization: $TOKEN"
else
    echo "Error: invalid number of arguments"
fi
