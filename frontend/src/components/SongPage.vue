<template>
  <v-app>
    <v-container>
      <v-row class="x-row grey lighten-5" align="start" justify="center">
        <h1 class="display-2 font-weight-bold mb-3">
          What am I listening to?
        </h1>
      </v-row>
    </v-container>
    <v-container>
      <v-row class="x-row grey lighten-5" align="start">
        <v-col cols=6 align="right">
            <v-img width="300" :src=song.coverImage>
            </v-img>
        </v-col>
        <v-col cols=3 align-self=center>
          <h3>
            Song: {{ song.name }}
          </h3>
          <h3>
            Artist(s): 
            <a v-for="(artist,i) in song.artists" :key="i">
              {{ artist }}<span v-if="i != song.artists.length - 1">, </span>
            </a>
          </h3>
          <h3>
            Album: {{ song.album }}
          </h3>
          <h3>
            Year: {{ song.releaseYear }}
          </h3>
          <h3>
            Genre: {{ song.genre }}
          </h3> 
        </v-col>
      </v-row>
      <v-row class="mt-8" justify="center">
        <h1 class="display-2 font-weight-bold mb-3">
          What is this?
        </h1>
      </v-row>
      <v-row>
        <h3>
          Well, if you know anything about me, I'm pretty much listening to music all day everyday. I'm using this page to show what my favorite song is at the moment. Hope you can find a new favorite song here :)
        </h3>
      </v-row>
      <v-row class="mt-8" justify="center">
        <h1>
          How does it work?
        </h1>
      </v-row>
      <v-row>
        <h3>
          This site has a few APIs running in the backend. The POST version of the API adds a song to the database, and then the GET version of the API retrieves the most recently added song from the database. The POST API requires a JWT that can only be acquired through a different login API, so only I can hit that API.
        </h3>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
  import axios from "axios"

  export default {
    data: () => ({
      song: {}
    }),

    mounted() {
      axios.get('/api/song').then(response => (this.song = response.data))
    }
  }
</script>

<style scoped>
  h3 {
    text-align: center;
  }
</style>
