<template>
  <v-app>
    <v-main>
      <HelloWorld/>
    </v-main>
  </v-app>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import axios from "axios"

export default {
  name: 'App',

  components: {
    HelloWorld,
  },

  data: () => ({
    //
  }),

  mounted() {
    axios.get('/api/check')
  }
}
</script>
