<template>
    <v-container class="pa-4" style="max-width: 400px;">
      <v-card>
        <v-card-title class="d-flex justify-center">
          <h2>{{ formatDate(props.log.done_date) }}</h2>
        </v-card-title>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" link :to="`/workout/${props.log.workout_id}/log/${props.log.id}`">View</v-btn>
          <!-- <v-btn color="secondary" link :to="`/workout/${props.log.workout_id}/log/${props.log.id}`">Log</v-btn> -->
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-container>
  </template>

<script setup lang="ts">
import type { MiniLog } from '@/types/workout'

const props = defineProps<{
    log: MiniLog
}>()

const formatDate = (date:Date):string => {
  const options: Intl.DateTimeFormatOptions = { month: 'long', day: 'numeric', year: 'numeric'}
  const dateString = date.toLocaleString('en-US', options)
  console.log(dateString)
  return dateString
}

</script>

<style scoped></style>
