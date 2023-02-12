<template>
  <v-app>
    <v-container>
      <v-row class="x-row grey lighten-5" align="start" justify="center">
        <h1 class="display-2 font-weight-bold mb-3">
          What am I listening to???????????
        </h1>
      </v-row>
      <v-row class="x-row grey lighten-5" align="start" justify="center">
        <h2>
          {{ song.name }}
        </h2>
      </v-row>
      <v-row align="start" justify="center">
        <div class="ma 4">
          <v-img width="300" :src=song.coverImage>
          </v-img>
        </div>
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
