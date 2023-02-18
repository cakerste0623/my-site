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
        </v-col>
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
