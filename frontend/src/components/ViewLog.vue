<template>
  <v-card class="mx-auto pa-6" elevation="15" max-width="800" rounded="lg">
    <div class="text-h3">{{ props.workout.name }}</div>
    <v-divider></v-divider>
    <v-list>
      <v-list-item v-if="contentLoaded" v-for="(e, ei) in exercises" :key="ei">
        <div class="text-h4">{{ e.name }}<v-icon icon="mdi-chevron-right"></v-icon></div>
        <v-row>
          <v-col v-for="(s, si) in e.sets" :key="si" cols="6">
            <div class="py-3">
              <v-card class="mx-auto pa-3" elevation="3" max-width="300" rounded="md">
                <div class="text-body-1">
                  {{ si + 1 }}. Reps: {{ s.reps }}/{{ goalExercises[ei].sets[si].reps }}<v-icon icon="mdi-counter"></v-icon> Weight:
                  {{ s.weight }}/{{ goalExercises[ei].sets[si].reps }}<v-icon icon="mdi-weight-pound"></v-icon>
                </div>
              </v-card>
            </div>
          </v-col>
        </v-row>
      </v-list-item>
    </v-list>
  </v-card>
</template>

<script setup lang="ts">
import { type Workout, type Exercise, convertSetsToExercises } from '@/types/workout'
import type { Ref } from 'vue'
import { onUpdated, ref } from 'vue'

const exercises: Ref<Exercise[]> = ref([])
const goalExercises: Ref<Exercise[]> = ref([])
const contentLoaded = ref(false)

const props = defineProps<{
  workout: Workout
  goalWorkout: Workout
}>()

onUpdated(() => {
  console.log(props.workout)
  exercises.value = convertSetsToExercises(props.workout.sets)
  goalExercises.value = convertSetsToExercises(props.goalWorkout.sets)
  console.log(props.goalWorkout)
  console.log(exercises.value)
  contentLoaded.value = true
})
</script>
