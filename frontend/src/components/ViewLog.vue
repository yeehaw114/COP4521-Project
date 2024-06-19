<template>
  <v-card class="mx-auto pa-6" elevation="15" max-width="800" rounded="lg">
    <div class="text-h3">{{ props.name }} <v-icon icon="mdi-at"/> {{ formatTime(String(props.time)) }}</div>
    <v-divider></v-divider>
    <v-list>
      <v-list-item v-for="(e, ei) in props.logged" :key="ei">
        <div class="text-h4">{{ e.name }}<v-icon icon="mdi-chevron-right"></v-icon></div>
        <v-row>
          <v-col v-for="(s, si) in e.sets" :key="si" cols="6">
            <div class="py-3">
              <v-card class="mx-auto pa-3" elevation="3" max-width="300" rounded="md">
                <div class="text-body-1">
                  {{ si + 1 }}. Reps: <span :style="{ color: s.reps < props.goal[ei].sets[si].reps ? 'red' : 'green'}">{{ s.reps }}</span>/{{ props.goal[ei].sets[si].reps }}<v-icon icon="mdi-counter"></v-icon> Weight:
                  <span :style="{ color: s.weight < props.goal[ei].sets[si].weight ? 'red' : 'green'}">{{ s.weight }}</span>/{{ props.goal[ei].sets[si].weight }}<v-icon icon="mdi-weight-pound"></v-icon>
                </div>
              </v-card>
            </div>
          </v-col>
        </v-row>
      </v-list-item>
    </v-list>
  </v-card>
</template>

<script setup lang="ts">
import { type Exercise } from '@/types/workout'
import { formatTime } from '@/helpers/format'

const props = defineProps<{
  name: string
  time: Date
  goal: Exercise[]
  logged: Exercise[]
}>()
</script>
