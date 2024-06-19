<template>
  <v-container class="pa-4" style="max-width: 400px">
    <v-card>
      <v-card-title class="d-flex justify-center">
        <h2>{{ formatDate(props.log.done_date) }}</h2>
      </v-card-title>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
          color="primary"
          prepend-icon="mdi-eye-circle-outline"
          link
          :to="`/workout/${props.log.workout_id}/log/${props.log.id}`"
          >View</v-btn
        >
        <v-btn color="red" prepend-icon="mdi-delete-outline" link @click="deleteWork">Delete</v-btn>
        <!-- <v-btn color="secondary" link :to="`/workout/${props.log.workout_id}/log/${props.log.id}`">Log</v-btn> -->
        <v-spacer></v-spacer>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script setup lang="ts">
import { deleteWorkout } from '@/requests/workout'
import type { MiniLog } from '@/types/workout'

const props = defineProps<{
  log: MiniLog
}>()

const emits = defineEmits<{
  delete: null[]
}>()

const deleteWork = async () => {
  try {
    await deleteWorkout(props.log.id)
    emits('delete')
    console.log('deleting...')
  } catch (error) {
    console.error(error)
  }
}

const formatDate = (date: Date): string => {
  const dateDate = new Date(date)
  const options: Intl.DateTimeFormatOptions = { month: 'long', day: '2-digit', year: 'numeric' }
  const formattedDate = dateDate.toLocaleDateString('en-US', options)
  return formattedDate
}
</script>

<style scoped></style>
