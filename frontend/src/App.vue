<template>
  <v-app>
    <v-main>
      <v-app-bar
      class="bg-red-lighten-1"
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
        <v-list-item prepend-icon="mdi-file-account" title="Resume" value="resume" link @click="$router.push({ path: '/resume' })"></v-list-item>
      </v-list>
    </v-navigation-drawer>
    </v-main>
    <router-view />
    <v-footer class="bg-red-lighten-1 text-center flex-column">
      <div>
        <v-btn class="mx-16" icon="mdi-linkedin" variant="text" key="mdi-linkedin" href="https://www.linkedin.com/in/collin-kersten-6236221aa/" target="_blank"></v-btn>
        <v-btn class="mx-16" icon="mdi-twitter" variant="text" key="mdi-twitter" href="https://twitter.com/CollinKersten" target="_blank"></v-btn>
        <v-btn class="mx-16" icon="mdi-github" variant="text" key="mdi-github" href="https://github.com/cakerste0623" target="_blank"></v-btn>
      </div>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  name: 'App',

  components: {

  },

  data: () => ({
    drawer: false
  }),

  mounted() {
  }
}
</script>
