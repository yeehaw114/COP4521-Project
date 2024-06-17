<template>
  <UserContent v-if="userStore.isLoggedIn"/>
  <LoggedOut v-else/>
</template>

<script setup lang="ts">
import UserContent from '@/components/UserContentView.vue'
import LoggedOut from '@/components/LoggedOutView.vue'
import { useUserStore } from '@/stores/user'
import { onMounted, ref } from 'vue'

const userStore = ref(useUserStore())

onMounted(() => {
  console.log(userStore.value.isLoggedIn)
})

</script>

<style scoped></style>
