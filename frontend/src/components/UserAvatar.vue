<template>
  <v-avatar color="red" size="large">
    <span class="text-h6">{{ username[0].toUpperCase() }}</span>
  </v-avatar>
  <span class="text-h7">@{{ username }}</span>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useUserStore } from '@/stores/user'
const userStore = useUserStore()
const username = computed(() => userStore.user?.username ?? '')
</script>
