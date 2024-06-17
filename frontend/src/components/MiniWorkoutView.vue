<template>
  <v-container class="pa-4" style="max-width: 400px">
    <v-card>
      <v-card-title class="d-flex justify-center">
        <h2>{{ props.workout.name }}</h2>
      </v-card-title>
      <v-card-actions v-if="props.template">
        <v-spacer></v-spacer>
        <v-btn color="primary" link :to="`/workout/${props.workout.id}`">View</v-btn>
        <v-btn color="secondary" link :to="`/workout/${props.workout.id}/log`">Log</v-btn>
        <v-spacer></v-spacer>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script setup lang="ts">
import type { MiniWorkout } from '@/types/workout'

const props = defineProps<{
  workout: MiniWorkout
  template?: boolean
  log?: boolean
}>()

const formatDate = (date: Date): string => {
  const options: Intl.DateTimeFormatOptions = { month: 'long', day: 'numeric', year: 'numeric' }
  const dateString = date.toLocaleString('en-US', options)
  console.log(dateString)
  return dateString
}
</script>

<style scoped></style>
