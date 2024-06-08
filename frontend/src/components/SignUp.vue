<template>
  <div>
    <v-card class="mx-auto pa-12" elevation="10" max-width="450" rounded="lg">
      <div class="text-subtitle-1 text-medium-emphasis">First Name</div>
      <v-text-field
        density="compact"
        placeholder="First name (e.g. John)"
        prepend-inner-icon="mdi-account-outline"
        variant="outlined"
      ></v-text-field>
      <div class="text-subtitle-1 text-medium-emphasis">Last Name</div>
      <v-text-field
        density="compact"
        placeholder="Last name (e.g. Smith)"
        prepend-inner-icon="mdi-account-outline"
        variant="outlined"
      ></v-text-field>
      <div class="text-subtitle-1 text-medium-emphasis">Email</div>
      <v-text-field
        density="compact"
        placeholder="Email name (e.g. john@mail.com)"
        prepend-inner-icon="mdi-email"
        variant="outlined"
      ></v-text-field>
      <div class="text-subtitle-1 text-medium-emphasis">Username</div>
      <v-text-field
        density="compact"
        placeholder="Username"
        prepend-inner-icon="mdi-badge-account-horizontal"
        variant="outlined"
      ></v-text-field>
      <div class="text-subtitle-1 text-medium-emphasis">Password</div>
      <v-text-field
        :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
        :type="visible ? 'text' : 'password'"
        density="compact"
        placeholder="Enter your password"
        prepend-inner-icon="mdi-lock-outline"
        variant="outlined"
        @click:append-inner="visible = !visible"
      ></v-text-field>
      <v-btn class="mb-8" color="green" size="large" variant="tonal" block>Sign Up</v-btn>
    </v-card>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const visible = ref(false)
</script>
