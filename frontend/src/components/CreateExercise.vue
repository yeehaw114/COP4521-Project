<template>
    <div class="text-subtitle-1 text-medium-emphasis">Exercise Name</div>
    <v-text-field
      density="compact"
      placeholder="Name"
      prepend-inner-icon="mdi-tag-text-outline"
      variant="outlined"
    ></v-text-field>
  <div class="text-subtitle-1 text-medium-emphasis">Number of sets</div>
  <v-slider
    prepend-icon="mdi-weight-lifter"
    v-model="numSets"
    step="1"
    min="1"
    max="8"
    thumb-label
  ></v-slider>
  <v-list>
    <v-list-items v-for="n in numSets" :key="n">
        <div>
        <div class="text-subtitle-1 text-medium-emphasis">Weight of set #{{ n }}</div>    
      <v-slider
        prepend-icon="mdi-weight-pound"
        v-model="weightNums[n-1]"
        step="5"
        min="5"
        max="500"
        thumb-label
      ></v-slider>
    </div>
    </v-list-items>
  </v-list>
</template>

<script setup lang="ts">
import { ref } from 'vue'
const numSets = ref(0)
const weightNums = ref([])
</script>
