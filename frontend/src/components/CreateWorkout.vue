<template>
  <v-card class="mx-auto pa-12" elevation="10" max-width="450" rounded="lg">
    <div class="text-subtitle-1 text-medium-emphasis">Name of Workout</div>
    <v-text-field
      density="compact"
      placeholder="Name"
      prepend-inner-icon="mdi-tag-text-outline"
      variant="outlined"
    ></v-text-field>
    <v-divider></v-divider>
    <div class="text-subtitle-1 text-medium-emphasis">Number of exercises</div>
    <v-slider
      prepend-icon="mdi-weight-lifter"
      v-model="numExercises"
      step="1"
      min="1"
      max="10"
      thumb-label
    ></v-slider>
    <v-list>
      <v-list-item v-for="n in numExercises" :key="n">
        <Exercise :ExerciseNum="n" />
      </v-list-item>
    </v-list>
  </v-card>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import Exercise from './CreateExercise.vue'

const numExercises = ref(1)
</script>
