<template>
  <v-card class="mx-auto pa-6" elevation="15" max-width="800" rounded="lg">
    <v-text-field
      v-model="workout.name"
      placeholder="New Workout"
      label="Name of Workout"
      required
    ></v-text-field>
    <!-- All the exercises -->
    <div class="text-subtitle-1 text-medium-emphasis">Exercises</div>
    <v-list>
      <v-list-item v-for="e in exercises" :key="e.name">
        <div class="text-h4">{{ e.name }}</div>
        <!-- New set -->
        <v-card>
          <v-row>
            <v-col>
              <VNumberInput
                inset
                :min="1"
                label="Reps"
                v-model="newSet.reps"
                control-variant="stacked"
              ></VNumberInput>
            </v-col>
            <v-col>
              <VNumberInput
                :min="1"
                inset
                label="Weight (lbs)"
                v-model="newSet.weight"
                :step="5"
                control-variant="split"
              ></VNumberInput>
            </v-col>
            <v-col>
              <v-btn rounded="0" icon="mdi-plus" @click="appendSet(e)"></v-btn>
            </v-col>
          </v-row>
          <div class="text-subtitle-2 text-medium-emphasis">Sets</div>
          <v-list>
            <v-list-item v-for="(s, i) in e.sets" :key="i">
              <div class="text-h8">
                {{ i + 1 }}<v-icon icon="mdi-chevron-right"></v-icon> Reps: {{ s.reps
                }}<v-icon icon="mdi-weight-lifter"></v-icon> Weight: {{ s.weight }}
                <v-icon icon="mdi-weight-pound"></v-icon>
              </div>
            </v-list-item>
          </v-list>
        </v-card>
      </v-list-item>
    </v-list>
    <v-row align="center">
      <v-col>
        <v-text-field v-model="newExercise.name" label="New Exercise" outlined></v-text-field>
      </v-col>
      <v-col cols="auto">
        <v-btn rounded="0" icon="mdi-plus" @click="appendExercise"></v-btn>
      </v-col>
    </v-row>
    <v-btn class="mb-8" color="green" size="large" variant="tonal" @click="createWorkout" block
      >Create</v-btn
    >
    <Error v-if="errorOccured" text="Could not create workout." />
  </v-card>

  <SuccessfulSnackbar v-model="success" text="Successfully posted workout" />
</template>

<script setup lang="ts">
import { ref } from 'vue'
import type { Ref } from 'vue'
import type { Workout, Set, Exercise } from '@/types/workout'
import { VNumberInput } from 'vuetify/labs/components'
import { postWorkout } from '@/requests/workout'
import Error from '@/components/ErrorComponent.vue'
import { useRouter } from 'vue-router'
import SuccessfulSnackbar from './SuccessfulSnackbar.vue'

const errorOccured = ref(false)
const success = ref(false)

const workout: Ref<Workout> = ref<Workout>({
  name: '',
  sets: [],
  id: 0
})

const router = useRouter()

const exercises: Ref<Exercise[]> = ref([])

const newExercise: Ref<Exercise> = ref({
  name: '',
  sets: []
})

const newSet: Ref<Set> = ref({
  exercise: '',
  id: 0,
  reps: 10,
  weight: 50
})

const appendSet = (e: Exercise) => {
  const copy = JSON.parse(JSON.stringify(newSet.value))
  copy.exercise = e.name
  e.sets.push(copy)
}

const appendExercise = () => {
  const name = newExercise.value.name
  if (name == '' || exercises.value.findIndex((i) => i.name === name) != -1) {
    return
  }

  const copy = JSON.parse(JSON.stringify(newExercise.value))
  exercises.value.push(copy)
  newExercise.value.name = ''
}

const convertToWorkout = () => {
  for (const e of exercises.value) {
    for (const s of e.sets) {
      const copy = JSON.parse(JSON.stringify(s))
      workout.value.sets.push(copy)
    }
  }
}

const createWorkout = async () => {
  convertToWorkout()
  try {
    await postWorkout(workout.value)
    success.value = true
    router.push('/')
  } catch (e) {
    errorOccured.value = true
  }
}
</script>
