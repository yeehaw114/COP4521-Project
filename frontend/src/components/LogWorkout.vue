<template>
  <v-card v-if="contentLoaded" class="mx-auto pa-6" elevation="15" max-width="800" rounded="lg">
    <div class="text-h3">{{ workout.name }}</div>
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
                  :max="goalExercises[ei].sets[si].reps"
                >
                  <template v-slot:append>
                    <v-text-field
                      v-model="s.reps"
                      density="compact"
                      style="width: 100px"
                      :min="0"
                      :max="goalExercises[ei].sets[si].reps"
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
                  :max="goalExercises[ei].sets[si].weight"
                >
                  <template v-slot:append>
                    <v-text-field
                      v-model="s.weight"
                      step="5"
                      density="compact"
                      style="width: 100px"
                      :min="0"
                      :max="goalExercises[ei].sets[si].weight"
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
    <Error v-if="errorOccured" text="Could not log workout"/>
    <v-btn class="mb-8" color="green" size="large" variant="tonal" @click="log" block>Log</v-btn>
  </v-card>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import type { Ref } from 'vue'
import { postLog } from '@/requests/log' 
import type { Workout, Set, Exercise } from '@/types/workout'
import Error from '@/components/ErrorComponent.vue'
import { useRoute } from 'vue-router';
import { getWorkout } from '@/requests/workout';

const workout:Ref<Workout> = ref({
  name: '',
  sets: [],
})


const workoutid:Ref<number> = ref(0)

const goalExercises:Ref<Exercise[]> = ref([])
const loggedExercises:Ref<Exercise[]> = ref([])

const contentLoaded = ref(false)
const errorOccured = ref(false)

const convertSetsToExercises = ():Exercise[] => {
  const exerciseMap: Map<string, Exercise> = workout.value.sets.reduce((map, set) => {
    if (!map.has(set.exercise)) {
      map.set(set.exercise, { name: set.exercise, sets: [] })
    }
    map.get(set.exercise)?.sets.push({ exercise: set.exercise, reps: set.reps, weight: set.weight })
    return map
  }, new Map<string, Exercise>())
  return Array.from(exerciseMap.values()) as Exercise[]
}

const log = async() => {
  try {
    await postLog(workoutid.value, workout.value)
  } catch(error) {
    console.error(error)
    errorOccured.value = true
  }
}

onMounted(async() => {
  try {
    workoutid.value = parseInt(useRoute().params.workoutid[0])
    if(isNaN(workoutid.value)) {
      throw new Error("Invalid workout id")
    }
    try {
      workout.value = await getWorkout(workoutid.value)
      goalExercises.value = convertSetsToExercises()
      loggedExercises.value = JSON.parse(JSON.stringify(goalExercises.value))
      contentLoaded.value = true
    } catch(error) {
      console.error(error)
    }
  } catch(error) {
    console.error(error)
  }
})

</script>
