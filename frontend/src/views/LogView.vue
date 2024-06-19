<template v-if="contentLoaded">
    <ViewLog :time="time" :name="name" :goal="goalExercises" :logged="loggedExercises" />
    <Error v-if="errorOccured" text="Error occurred"/>
  </template>
  
  <script setup lang="ts">
  import { onMounted, ref } from 'vue'
  import { useRoute } from 'vue-router'
  import { convertSetsToExercises, type Workout, type Exercise } from '@/types/workout'
  import type { Ref } from 'vue'
  import { getWorkout } from '@/requests/workout'
  import { stringArrayToInt } from '@/helpers/convert'
  import ViewLog from '@/components/ViewLog.vue'
  import { getLog } from '@/requests/log'
  import Error from '@/components/ErrorComponent.vue'
  
  const contentLoaded = ref(false)
  const errorOccured = ref(false)

  const name = ref("")
  const time:Ref<Date> = ref(new Date())
  const goalExercises:Ref<Exercise[]> = ref([])
  const loggedExercises:Ref<Exercise[]> = ref([])
  
  onMounted(async () => {
    try {
      const workoutid = stringArrayToInt(useRoute().params.workoutid as string[])
      const logid = stringArrayToInt(useRoute().params.logid as string[])

      const goalWorkout = await getWorkout(workoutid)
      goalExercises.value = convertSetsToExercises(goalWorkout.sets)
      console.log(goalExercises.value)
      const loggedWorkout = await getLog(logid)
      time.value = loggedWorkout.done_date
      loggedExercises.value = convertSetsToExercises(loggedWorkout.sets)
      console.log(loggedExercises.value)

      name.value = loggedWorkout.name

      contentLoaded.value = true
    } catch(error) {
        errorOccured.value =  true
        console.error(error)
    }
  })
  </script>
  