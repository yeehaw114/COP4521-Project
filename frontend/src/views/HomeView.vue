<script setup lang="ts">
import { ref, onMounted } from 'vue';

// Create refs for data and loading state
const data = ref<Workout[]>([]);
const dataLoaded = ref(false);

// Function to fetch data
const getData = async (): Promise<void> => {
  try {
    const response = await fetch("http://localhost:8000/api/workouts/");
    if (!response.ok) {
      throw new Error("Failed to fetch data");
    }
    const workouts: Workout[] = await response.json();
    data.value = workouts;
    dataLoaded.value = true;
  } catch (error) {
    console.warn(error.message);
  }
};

// Fetch data when component is mounted
onMounted(() => {
  getData();
});
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
