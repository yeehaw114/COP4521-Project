<template>
    <LogWorkout
      v-if="contentLoaded"
      :workoutid="workoutid"
      :name="workout.name"
      :goalExercises="exercises"
      :loggedExercises="JSON.parse(JSON.stringify(exercises))"
    />
  </template>
  
  <script setup lang="ts">
  import LogWorkout from '@/components/LogWorkout.vue'
  import type { Workout, Exercise } from '@/types/workout'
  import type { Ref } from 'vue'
  import { convertSetsToExercises } from '@/types/workout'
  import { ref, onMounted } from 'vue'
  import { useRoute } from 'vue-router'
  import { getWorkout, stringArrayToInt } from '@/requests/workout'
  
  const workoutid: Ref<number> = ref(0)
  const logid: Ref<number> = ref(0)

  const workoutExercises: Ref<Exercise[]> = ref([])
  const loggedExercises: Ref<Exercise[]> = ref([])
  const contentLoaded = ref(false)
  const workout: Ref<Workout> = ref({
    name: '',
    id: 0,
    sets: []
  })
  
  onMounted(async () => {
    try {
      workoutid.value = stringArrayToInt(useRoute().params.workoutid as string[])
      logid.value = stringArrayToInt(useRoute().params.logid as string[])
      try {
        if (isNaN(workoutid.value)) {
          throw new Error('Invalid workout id')
        }
        workout.value = await getWorkout(workoutid.value)
        logWorkout.value = await getLog(logid.value)

        workoutExercises.value = convertSetsToExercises(workout.value.sets)
        loggedExercises.value = convertExercisesToSets(logWorkout.value.sets)
        
        contentLoaded.value = true
      } catch (error) {
        console.error(error)
      }
      console.log('workoutid: ' + workoutid.value)
    } catch (error) {
      console.error(error)
    }
  })
  </script>
  
  <style scoped></style>
  