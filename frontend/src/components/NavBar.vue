<template>
  <v-navigation-drawer :width="200" :close-delay="200" absolute rail expand-on-hover>
    <v-list>
      <v-list-item prepend-icon="mdi-dumbbell" :title="config.appTitle"></v-list-item>
    </v-list>
    <v-divider></v-divider>
    <v-list>
      <v-list-item prepend-icon="mdi-home" link to="/" title="Home"></v-list-item>
      <v-list-item prepend-icon="mdi-information" link to="/about" title="About"></v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script setup lang="ts">
import config from '../../config.json'
</script>

<style scoped></style>
