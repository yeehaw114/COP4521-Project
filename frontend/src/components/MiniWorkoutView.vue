<template>
    <v-container class="pa-4" style="max-width: 400px;">
      <v-card>
        <v-card-title class="d-flex justify-center">
          <h2>{{props.workout.name}}</h2>
        </v-card-title>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" @click="view">View</v-btn>
          <v-btn color="secondary" @click="log">Log</v-btn>
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-container>
  </template>

<script setup lang="ts">
import type { Workout } from '@/types/workout'

const props = defineProps<{
  workout:Workout
}>()

const view = () => {

}

const log = () => {

}

</script>

<style scoped></style>
