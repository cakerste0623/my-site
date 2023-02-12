<template>
  <v-container>
    <v-row class="text-center">
      <v-col class="mb-4">
        <h1 class="display-2 font-weight-bold mb-3">
          What am I listening to?: {{ song.name }}
        </h1>
      </v-col>
    </v-row>
  </v-container>
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
