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
        <v-col cols=3>
          <h3 align="center">
            Song: {{ song.name }}
          </h3>
          <h3 align="center">
            Artist: {{ song.artist }}
          </h3>
          <h3 align="center">
            Album: {{ song.album }}
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
