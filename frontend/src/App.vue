<template>
  <v-app>
    <div>
      <NavBar />
    </div>
    <div>
      <v-main>
        <v-container fluid>
          <RouterView />
        </v-container>
      </v-main>
    </div>
  </v-app>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';
import { getToken } from './requests/auth';
import { RouterView } from 'vue-router'
import NavBar from '@/components/NavBar.vue'

onMounted(async()=> { await getToken() })


</script>

<style scoped></style>
