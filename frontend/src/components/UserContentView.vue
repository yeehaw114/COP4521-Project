<template>
  <Error v-if="errorOccured" text="Could not load resources." />
  <div v-if="contentLoaded">
    <div class="text-h4">My Workouts</div>
    <v-col v-for="w in userWorkouts" cols="12">
      <MiniWorkoutView :workout="w" />
    </v-col>
    <div class="text-h6" v-if="userWorkouts.length == 0">No workouts created yet.</div>
    <div class="text-h4">My Logs</div>
    <div v-for="l in userLogs" cols="12">
      <MiniLogView :log="l" />
    </div>
    <div class="text-h6" v-if="userLogs.length == 0">No workouts logged yet.</div>
    <div></div>
  </div>
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

const contentLoaded = ref(false)
const errorOccured = ref(false)
const userWorkouts: Ref<MiniWorkout[]> = ref([])
const userLogs: Ref<MiniLog[]> = ref([])

onMounted(async () => {
  try {
    userLogs.value = await getUserLogs()
    userWorkouts.value = await getUserWorkouts()
  } catch (error) {
    errorOccured.value = true
    console.error(error)
  } finally {
    contentLoaded.value = true
  }
})
</script>

<style scoped></style>
