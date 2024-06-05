<template>
  <div class="text-subtitle-1 text-medium-emphasis">Exercise #{{ props.ExerciseNum }} Name</div>
  <v-text-field
    density="compact"
    placeholder="Name"
    prepend-inner-icon="mdi-tag-text-outline"
    variant="outlined"
  ></v-text-field>
  <div class="text-subtitle-1 text-medium-emphasis">Number of sets</div>
  <v-slider
    prepend-icon="mdi-kettlebell"
    v-model="numSets"
    step="1"
    min="1"
    max="8"
    thumb-label
  ></v-slider>
  <v-list>
    <v-list-items v-for="n in numSets" :key="n">
      <div class="py-3">
        <v-card class="mx-auto pa-3" elevation="8" max-width="350" rounded="md">
          <div class="text-subtitle-1 text-medium-emphasis">Set #{{ n }}</div>
          <div class="text-subtitle-2 text-medium-emphasis">Reps</div>
          <v-slider
            prepend-icon="mdi-counter"
            v-model="repNums[n - 1]"
            step="1"
            min="1"
            max="30"
            thumb-label
          ></v-slider>
          <div class="text-subtitle-2 text-medium-emphasis">Weight</div>
          <v-slider
            prepend-icon="mdi-weight-pound"
            v-model="weightNums[n - 1]"
            step="5"
            min="5"
            max="500"
            thumb-label
          ></v-slider>
        </v-card>
      </div>
    </v-list-items>
  </v-list>
</template>

<script setup lang="ts">
import { ref } from 'vue'
const numSets = ref(1)
const weightNums = ref([])
const repNums = ref([])

const props = defineProps({
  ExerciseNum: {
    type: Number,
    required: true
  }
})
</script>
