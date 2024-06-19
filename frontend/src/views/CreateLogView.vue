<template>
  <LogWorkout
    v-if="contentLoaded"
    :workoutid="workoutid"
    :update=false
    :name="workout.name"
    :goalExercises="exercises"
    :loggedExercises="JSON.parse(JSON.stringify(exercises))"
    @action="post"
  />
  <Error v-if="errorOccurred" text="Could not post log"/>
</template>

<script setup lang="ts">
import LogWorkout from '@/components/LogWorkout.vue'
import type { Workout, Exercise, Set } from '@/types/workout'
import type { Ref } from 'vue'
import { convertSetsToExercises } from '@/types/workout'
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { getWorkout } from '@/requests/workout'
import { stringArrayToInt } from '@/helpers/convert'
import { postLog } from '@/requests/log'
import Error from '@/components/ErrorComponent.vue'

const errorOccurred = ref(false)
const workoutid: Ref<number> = ref(0)
const exercises: Ref<Exercise[]> = ref([])
const contentLoaded = ref(false)
const workout: Ref<Workout> = ref({
  name: '',
  id: 0,
  sets: []
})

const router = useRouter()

const post = async(sets: Set[]) => {
  try {
    errorOccurred.value = false
    await postLog(workoutid.value, sets)
    router.push('/')
  } catch(error) {
    errorOccurred.value = true
    console.error(error)
  }
}

onMounted(async () => {
  try {
    workoutid.value = stringArrayToInt(useRoute().params.workoutid as string[])
    try {
      if (isNaN(workoutid.value)) {
        throw new Error('Invalid workout id')
      }
      workout.value = await getWorkout(workoutid.value)
      exercises.value = convertSetsToExercises(workout.value.sets)
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
