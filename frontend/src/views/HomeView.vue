<template v-if="contentLoaded">

  <div v-for="w in userWorkouts">
    <h1>Sample Templates</h1>
    <MiniWorkout :workout="w"/>
  </div>
  <!-- <div>
    <v-row>
      <v-col>
        <v-sheet height="200">
          <v-calendar class="h-10 w-20" color="primary"></v-calendar>
        </v-sheet>
      </v-col>
    </v-row>
  </div> -->
</template>

<script setup lang="ts">
// import displayTemplate from '@/components/DisplayTemplate.vue'
import type { Ref } from 'vue'
import { ref, onMounted } from 'vue'
import type { Workout } from '@/types/workout'
import MiniWorkout from '@/components/MiniWorkoutView.vue'
import { VCalendar } from 'vuetify/labs/VCalendar'
import { getUserWorkouts } from '@/requests/workout'

const contentLoaded = ref(false)
const userWorkouts:Ref<Workout[]> = ref([])

onMounted(async() => {
  try {
    userWorkouts.value = await getUserWorkouts()
    contentLoaded.value = true
  } catch(error) {
    console.error(error)
  }
})

</script>

<style scoped></style>
