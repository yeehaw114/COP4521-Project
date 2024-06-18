<template v-if="contentLoaded">
    <ViewLog :goalWorkout="goalWorkout" :workout="workout" />
    <Error v-if="errorOccured"/>
  </template>
  
  <script setup lang="ts">
  import { onMounted, ref } from 'vue'
  import { useRoute } from 'vue-router'
  import type { Workout } from '@/types/workout'
  import type { Ref } from 'vue'
  import { getWorkout, stringArrayToInt } from '@/requests/workout'
  import ViewLog from '@/components/ViewLog.vue'
  import { getLog } from '@/requests/log'
  import ErrorComponent from '@/components/ErrorComponent.vue'
  
  const contentLoaded = ref(false)
  const errorOccured = ref(false)
  const workout: Ref<Workout> = ref({
    name: '',
    id: 0,
    sets: []
  })

  const goalWorkout: Ref<Workout> = ref({
    name: '',
    id: 0,
    sets: []
  })
  
  onMounted(async () => {
    try {
        const workoutid = stringArrayToInt(useRoute().params.workoutid as string[])
        workout.value = await getWorkout(workoutid)

        const logid = stringArrayToInt(useRoute().params.logid as string[])
        goalWorkout.value = await getLog(logid)
        
        contentLoaded.value = true
    } catch(error) {
        errorOccured.value =  true
        console.error(error)
    }
  })
  </script>
  