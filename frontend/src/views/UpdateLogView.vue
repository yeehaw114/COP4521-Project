<template>
  <LogWorkout
    v-if="contentLoaded"
    :workoutid="workoutid"
    update
    :name="name"
    :goalExercises="goalExercises"
    :loggedExercises="loggedExercises"
    @action="update"
  />
  <Error v-if="errorOccurred" text="Could not update log" />
</template>

<script setup lang="ts">
import LogWorkout from '@/components/LogWorkout.vue'
import type { Workout, Set, Exercise } from '@/types/workout'
import type { Ref } from 'vue'
import { convertSetsToExercises } from '@/types/workout'
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { getWorkout } from '@/requests/workout'
import { stringArrayToInt } from '@/helpers/convert'
import { getLog, updateLog } from '@/requests/log'
import Error from '@/components/ErrorComponent.vue'

const workoutid: Ref<number> = ref(0)
const logid: Ref<number> = ref(0)
const name = ref('')

const goalExercises: Ref<Exercise[]> = ref([])
const loggedExercises: Ref<Exercise[]> = ref([])
const contentLoaded = ref(false)
const errorOccurred = ref(false)

const router = useRouter()

const update = async (sets: Set[]) => {
  try {
    errorOccurred.value = false
    await updateLog(logid.value, sets)
    router.push('/')
  } catch (error) {
    errorOccurred.value = true
  }
}

onMounted(async () => {
  try {
    workoutid.value = stringArrayToInt(useRoute().params.workoutid as string[])
    logid.value = stringArrayToInt(useRoute().params.logid as string[])
    try {
      if (isNaN(workoutid.value) || isNaN(logid.value)) {
        throw new Error('Invalid workout id')
      }
      const goalWorkout: Workout = await getWorkout(workoutid.value)
      const logWorkout = await getLog(logid.value)

      name.value = goalWorkout.name
      goalExercises.value = convertSetsToExercises(goalWorkout.sets)
      loggedExercises.value = convertSetsToExercises(logWorkout.sets)

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
