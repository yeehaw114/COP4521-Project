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
import { RouterView } from 'vue-router'
import NavBar from '@/components/NavBar.vue'
import { onMounted } from 'vue'
import { tokenLogin } from './requests/auth'
import { setThemeFromLocalStorage } from './helpers/theme';
import { useTheme } from 'vuetify';

onMounted(async () => {
  setThemeFromLocalStorage(useTheme())
  await tokenLogin()
})
</script>

<style scoped></style>
