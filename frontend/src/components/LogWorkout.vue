<template>
  <v-card class="mx-auto pa-6" elevation="15" max-width="800" rounded="lg">
    <div class="text-h3">{{ props.name }}</div>
    <v-divider></v-divider>
    <v-list>
      <v-list-item v-for="(e, ei) in loggedExercises" :key="ei">
        <div class="text-h4">{{ e.name }}<v-icon icon="mdi-chevron-right"></v-icon></div>
        <v-row>
          <v-col v-for="(s, si) in e.sets" :key="si" cols="6">
            <div class="py-3">
              <v-card class="mx-auto pa-3" elevation="8" max-width="300" rounded="md">
                <div class="text-subtitle-1 text-medium-emphasis">Set {{ si + 1 }}</div>
                <div class="text-subtitle-2 text-medium-emphasis">Reps</div>
                <v-slider
                  prepend-icon="mdi-counter"
                  v-model="s.reps"
                  step="1"
                  :min="0"
                  :max="props.exercises[ei].sets[si].reps"
                >
                  <template v-slot:append>
                    <v-text-field
                      v-model="s.reps"
                      density="compact"
                      style="width: 100px"
                      :min="0"
                      :max="props.exercises[ei].sets[si].reps"
                      type="number"
                      hide-details
                    ></v-text-field>
                  </template>
                </v-slider>
                <div class="text-subtitle-2 text-medium-emphasis">Weight</div>
                <v-slider
                  prepend-icon="mdi-weight-pound"
                  v-model="s.weight"
                  step="5"
                  :min="0"
                  :max="props.exercises[ei].sets[si].weight"
                >
                  <template v-slot:append>
                    <v-text-field
                      v-model="s.weight"
                      step="5"
                      density="compact"
                      style="width: 100px"
                      :min="0"
                      :max="props.exercises[ei].sets[si].weight"
                      type="number"
                      hide-details
                    ></v-text-field>
                  </template>
                </v-slider>
              </v-card>
            </div>
          </v-col>
        </v-row>
      </v-list-item>
    </v-list>
    <Error v-if="errorOccured" text="Could not log workout" />
    <v-btn class="mb-8" color="green" size="large" variant="tonal" @click="log" block>Log</v-btn>
  </v-card>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import type { Ref } from 'vue'
import { postLog } from '@/requests/log'
import { type Workout, type Set, type Exercise, convertExercisesToSets } from '@/types/workout'
import Error from '@/components/ErrorComponent.vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const props = defineProps<{
  name: string
  exercises: Exercise[]
  workoutid: number
}>()

const workout: Ref<Workout> = ref({
  name: '',
  id: 0,
  sets: []
})

const loggedExercises: Ref<Exercise[]> = ref(JSON.parse(JSON.stringify(props.exercises)))

const errorOccured = ref(false)

const log = async () => {
  try {
    errorOccured.value = false
    const sets = convertExercisesToSets(loggedExercises.value)
    await postLog(props.workoutid, sets)
    router.push('/')
  } catch (error) {
    console.error(error)
    errorOccured.value = true
  }
}
</script>
