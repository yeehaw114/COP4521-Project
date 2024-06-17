<template>
  <LogWorkout v-if="contentLoaded" :workoutid="workoutid" :name="workout.name" :exercises="exercises" />
</template>

<script setup lang="ts">
import LogWorkout from '@/components/LogWorkout.vue'
import type { Workout, Exercise } from '@/types/workout'
import type { Ref } from 'vue'
import { convertSetsToExercises } from '@/types/workout'
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { getWorkout } from '@/requests/workout'

const workoutid:Ref<number> = ref(0)
const exercises:Ref<Exercise[]> = ref([])
const contentLoaded = ref(false)
const workout:Ref<Workout> = ref({
  name: '',
  id: 0,
  sets: []
})

onMounted(async () => {
  try {
    workoutid.value = parseInt(useRoute().params.workoutid[0])
    if (isNaN(workoutid.value)) {
      throw new Error('Invalid workout id')
    }
    try {
      workout.value = await getWorkout(workoutid.value)
      exercises.value = convertSetsToExercises(workout.value.sets)
      contentLoaded.value = true
    } catch (error) {
      console.error(error)
    }
  } catch (error) {
    console.error(error)
  }
})

</script>

<style scoped></style>
