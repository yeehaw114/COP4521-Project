<template>
  <v-container class="pa-4" style="max-width: 400px">
    <v-card>
      <v-card-title class="d-flex justify-center">
        <h2>{{ formatTime(String(props.log.done_date)) }}</h2>
      </v-card-title>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="secondary" prepend-icon="mdi-update" link :to="`/workout/${props.log.workout_id}/log/${props.log.id}/update`">Update</v-btn>
        <v-btn
          color="primary"
          prepend-icon="mdi-eye-circle-outline"
          link
          :to="`/workout/${props.log.workout_id}/log/${props.log.id}`"
          >View</v-btn
        >
        <v-btn color="red" prepend-icon="mdi-delete-outline" link @click="delLog">Delete</v-btn>
        <v-spacer></v-spacer>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script setup lang="ts">
import { deleteLog } from '@/requests/log'
import type { MiniLog } from '@/types/workout'
import { formatTime } from '@/helpers/format';

const props = defineProps<{
  log: MiniLog
}>()

const emits = defineEmits<{
  delete: null[]
}>()

const delLog = async () => {
  try {
    await deleteLog(props.log.id)
    emits('delete')
    console.log('deleting...')
  } catch (error) {
    console.error(error)
  }
}

</script>

<style scoped></style>
