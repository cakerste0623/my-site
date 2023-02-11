<template>
  <v-app>
    <v-main>
      <v-app-bar
      color="primary"
      density="compact"
      >
        <v-app-bar-nav-icon variant="text" @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
        <v-app-bar-title>Welcome</v-app-bar-title>
      </v-app-bar>
    <v-navigation-drawer
      v-model="drawer"
      location="left"
      temporary
    >
      <v-list>
        <v-list-item prepend-icon="mdi-home-city" title="Home" value="home" link @click="$router.push({ path: '/' })"></v-list-item>
        <v-list-item prepend-icon="mdi-music" title="What am I listening to?" value="song" link @click="$router.push({ path: '/song' })"></v-list-item>
        <v-list-item prepend-icon="mdi-file-account" title="Resume" value="resume"></v-list-item>
      </v-list>
    </v-navigation-drawer>
    </v-main>
    <router-view />
  </v-app>
</template>

<script>
import axios from "axios"

export default {
  name: 'App',

  components: {

  },

  data: () => ({
    drawer: false
  }),

  mounted() {
    axios.get('/api/check')
  }
}
</script>
