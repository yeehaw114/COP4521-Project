<template>
  <LogWorkout :workout="w" />
</template>

<script setup lang="ts">
import LogWorkout from '@/components/LogWorkout.vue'
import type { Workout } from '@/types/workout'

const w: Workout = {
  name: 'Push Day',
  sets: [
    {
      exercise: 'Bench press',
      reps: 10,
      weight: 100
    },
    {
      exercise: 'Bench press',
      reps: 10,
      weight: 100
    },
    {
      exercise: 'Bench press',
      reps: 10,
      weight: 100
    },
    {
      exercise: 'Bench press',
      reps: 10,
      weight: 100
    },
    {
      exercise: 'Shoulder press',
      reps: 10,
      weight: 50
    },
    {
      exercise: 'Shoulder press',
      reps: 10,
      weight: 50
    },
    {
      exercise: 'Shoulder press',
      reps: 10,
      weight: 50
    },
    {
      exercise: 'abs machine',
      reps: 30,
      weight: 80
    }
  ]
}
</script>

<style scoped></style>
