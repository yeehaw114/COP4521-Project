<template>
  <v-container class="pa-4" style="max-width: 350px">
    <v-card>
      <v-card-title class="d-flex justify-center">
        <h2>{{ props.workout.name }}</h2>
      </v-card-title>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
          color="secondary"
          prepend-icon="mdi-weight-lifter"
          link
          :to="`/workout/${props.workout.id}/log`"
          >Log</v-btn
        >
        <v-btn
          color="primary"
          prepend-icon="mdi-eye-circle-outline"
          link
          :to="`/workout/${props.workout.id}`"
          >View</v-btn
        >
        <v-btn color="red" prepend-icon="mdi-delete-outline" link @click="deleteWork">Delete</v-btn>
        <v-spacer></v-spacer>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script setup lang="ts">
import type { MiniWorkout } from '@/types/workout'
import { deleteWorkout } from '@/requests/workout'

const props = defineProps<{
  workout: MiniWorkout
}>()

const emits = defineEmits<{
  delete: null[]
}>()

const deleteWork = async () => {
  try {
    await deleteWorkout(props.workout.id)
    emits('delete')
  } catch (error) {
    console.error(error)
  }
}

const formatDate = (date: Date): string => {
  const options: Intl.DateTimeFormatOptions = { month: 'long', day: 'numeric', year: 'numeric' }
  const dateString = date.toLocaleString('en-US', options)
  console.log(dateString)
  return dateString
}
</script>

<style scoped></style>
