<template>
  <div>
    <h1>Your Templates</h1>
    <displayTemplate/>
  </div>
  <div>
    <h1>Sample Templates</h1>
    <displayTemplate/>
  </div>
  <div>
    <v-row>
      <v-col>
        <v-sheet height="200">
          <v-calendar color="primary" style="width: 600px;"></v-calendar>
        </v-sheet>
      </v-col>
    </v-row>
  </div>
</template>

<script setup lang="ts">
  import displayTemplate from "../components/DisplayTemplate.vue"
  import { VCalendar } from 'vuetify/labs/VCalendar'
</script>

<style scoped></style>
