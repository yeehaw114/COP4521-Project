<template>
  <Error v-if="errorOccured" text="Could not load resources." />
  <div v-if="contentLoaded">
    <div class="text-h4">My Workouts</div>
    <div class="text-h6 pb-3" v-if="userWorkouts.length == 0">No workouts created yet.</div>
    <v-row>
      <v-col v-for="w in userWorkouts" cols="4">
        <MiniWorkoutView @delete="refetchWorkouts" :workout="w" />
      </v-col>
    </v-row>
    <div class="text-h4 pt-3">My Logs</div>
    <div class="text-h6" v-if="userLogs.length == 0">No workouts logged yet.</div>
    <v-row>
      <v-col v-for="l in userLogs" cols="4">
        <MiniLogView @delete="refetchLogs" :log="l" />
      </v-col>
    </v-row>
    <div></div>
  </div>
  <SuccessfulSnackbar v-model="deleteWorkoutSuccess" text="Successfully deleted workout" />
  <SuccessfulSnackbar v-model="deleteLogSuccess" text="Successfully deleted log" />
</template>

<script setup lang="ts">
// import displayTemplate from '@/components/DisplayTemplate.vue'
import type { Ref } from 'vue'
import { ref, onMounted } from 'vue'
import type { Workout, MiniWorkout, MiniLog } from '@/types/workout'
import MiniWorkoutView from '@/components/MiniWorkoutView.vue'
import MiniLogView from '@/components/MiniLogView.vue'
import Error from '@/components/ErrorComponent.vue'
import { getUserWorkouts } from '@/requests/workout'
import { getUserLogs } from '@/requests/log'
import SuccessfulSnackbar from './SuccessfulSnackbar.vue'

const contentLoaded = ref(false)
const errorOccured = ref(false)
const userWorkouts: Ref<MiniWorkout[]> = ref([])
const userLogs: Ref<MiniLog[]> = ref([])

const deleteLogSuccess = ref(false)

const deleteWorkoutSuccess = ref(false)

const refetchLogs = async () => {
  userLogs.value = await getUserLogs()
  deleteLogSuccess.value = true
}

const refetchWorkouts = async () => {
  userWorkouts.value = await getUserWorkouts()
  userLogs.value = await getUserLogs()
  deleteWorkoutSuccess.value = true
}

onMounted(async () => {
  try {
    userLogs.value = await getUserLogs()
    userWorkouts.value = await getUserWorkouts()
    console.log(userLogs.value)
  } catch (error) {
    errorOccured.value = true
    console.error(error)
  } finally {
    contentLoaded.value = true
  }
})
</script>

<style scoped></style>
