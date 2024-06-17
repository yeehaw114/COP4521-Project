<script setup lang="ts">
import { ref } from 'vue';

// Define types for the data
interface Workout {
  id: number;
  name: string;
  description: string;
  created_at: string;
}

// Create refs for data and loading state
const data = ref<Workout[]>([]);
const dataLoaded = ref(false);

// Function to fetch data
const getData = async (): Promise<void> => {
  try {
    const response = await fetch("http://localhost:8080/api/workouts/");
    if (!response.ok) {
      throw new Error("Failed to fetch data");
    }
    const workouts: Workout[] = await response.json();  // Expecting the response to be an array of Workout objects
    data.value = workouts;  // Assigning the fetched workouts to the reactive ref
    dataLoaded.value = true;  // Setting dataLoaded to true indicating data has been loaded
  } catch (error) {
    console.warn(error.message);  // Logging any errors that occur during the fetch
  }
};

getData();

</script>

<template>
  <div>
    <div v-if="!dataLoaded">Loading...</div>
    <div v-else>
      <ul>
        <li v-for="workout in data" :key="workout.id">{{ workout.name }}</li>
      </ul>
    </div>
  </div>
</template>

<script setup lang="ts">
import displayTemplate from '../components/DisplayTemplate.vue'
import { VCalendar } from 'vuetify/labs/VCalendar'
</script>

<style scoped></style>
