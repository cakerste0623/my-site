<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <v-img
          :src="require('../assets/myself.jpg')"
          class="my-3"
          contain
          height="300"
        />
      </v-col>

      <v-col class="mx-16">
        <h1 class="display-2 font-weight-bold mb-3">
          Collin Kersten
        </h1>


        <p class="subheading font-weight-regular">
          I have a bachelor's degree in computer science with a concentration in cybersecurity. I have one year of experience in the software engineering field. I have experience working with Kubernetes, Helm, Azure, Docker, Jenkins, Ansible, Java, Python, and Bash. For my full resume, visit the resume page on this site.
        </p>
      </v-col>

      <v-col
        class="mb-5"
        cols="12"
      >
        <v-btn prepend-icon="mdi-email" append-icon="mdi-email" href="mailto:cak0623@gmail.com" class="my-12" size="x-large">
          Contact Me!
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>
