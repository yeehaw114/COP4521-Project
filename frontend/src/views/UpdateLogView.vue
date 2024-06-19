<template>
    <LogWorkout
      v-if="contentLoaded"
      :workoutid="workoutid"
      :name="name"
      :goalExercises="goalExercises"
      :loggedExercises="loggedExercises"
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
  import { getLog } from '@/requests/log'
  
  const workoutid: Ref<number> = ref(0)
  const logid: Ref<number> = ref(0)
  const name = ref("")

  const goalExercises: Ref<Exercise[]> = ref([])
  const loggedExercises: Ref<Exercise[]> = ref([])
  const contentLoaded = ref(false)
  
  onMounted(async () => {
    try {
      workoutid.value = stringArrayToInt(useRoute().params.workoutid as string[])
      logid.value = stringArrayToInt(useRoute().params.logid as string[])
      try {
        if (isNaN(workoutid.value) || isNaN(logid.value)) {
          throw new Error('Invalid workout id')
        }
        const goalWorkout:Workout = await getWorkout(workoutid.value)
        const logWorkout = await getLog(logid.value)

        name.value = goalWorkout.name
        goalExercises.value = convertSetsToExercises(goalWorkout.sets)
        loggedExercises.value = convertSetsToExercises(logWorkout[0].sets)
        
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
  