<template v-if="contentLoaded">
  <WorkoutComponent :workout="workout" />
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import type { Workout } from '@/types/workout'
import type { Ref } from 'vue'
import { getWorkout } from '@/requests/workout'
import { stringArrayToInt } from '@/helpers/convert'
import WorkoutComponent from '@/components/Workout.vue'

const contentLoaded = ref(false)
const workout: Ref<Workout> = ref({
  name: 'test',
  id: 0,
  sets: []
})

onMounted(async () => {
  const workoutid = stringArrayToInt(useRoute().params.workoutid as string[])
  workout.value = await getWorkout(workoutid)
  console.log(workout.value)
  contentLoaded.value = true
})
</script>
