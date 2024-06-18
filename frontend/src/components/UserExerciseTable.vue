<template>
  <v-table height="300px" fixed-header>
    <thead>
      <tr>
        <th class="text-left">Name</th>
        <th v-for="(s, index) in exercise.sets" :key="index">Set #{{ index }} Avg Reps</th>
        <th>Date</th>
      </tr>
    </thead>
  </v-table>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import type { Ref } from 'vue'
import type { Exercise } from '../types/exercise'

const exercise: Ref<Exercise> = ref({
  name: 'Bench Press',
  sets: [
    { reps: 10, weight: 100 },
    { reps: 10, weight: 100 },
    { reps: 8, weight: 100 },
    { reps: 7, weight: 100 }
  ],
  avgReps: 8.75,
  avgWeight: 100
})
</script>
