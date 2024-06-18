<template>
  <div>
    <v-card class="mx-auto pa-12" elevation="10" max-width="450" rounded="lg">
      <div class="text-subtitle-1 text-medium-emphasis">Email</div>
      <v-text-field
        v-model="creds.email"
        density="compact"
        placeholder="Email (e.g. john@mail.com)"
        prepend-inner-icon="mdi-email"
        variant="outlined"
        required
      ></v-text-field>
      <div class="text-subtitle-1 text-medium-emphasis">Username</div>
      <v-text-field
        v-model="creds.username"
        density="compact"
        placeholder="Username (e.g. john)"
        prepend-inner-icon="mdi-badge-account-horizontal"
        variant="outlined"
        required
      ></v-text-field>
      <div class="text-subtitle-1 text-medium-emphasis">Password</div>
      <v-text-field
        v-model="creds.password"
        :append-inner-icon="passwordVisible ? 'mdi-eye-off' : 'mdi-eye'"
        :type="passwordVisible ? 'text' : 'password'"
        density="compact"
        placeholder="Enter your password"
        prepend-inner-icon="mdi-lock-outline"
        variant="outlined"
        required
        @click:append-inner="passwordVisible = !passwordVisible"
      ></v-text-field>
      <div class="text-subtitle-1 text-medium-emphasis">Account Tier</div>
      <v-col class="py-2" cols="12">
        <v-btn-toggle v-model="creds.role" color="teal-lighten-2" rounded="3" group>
          <v-btn prepend-icon="mdi-account-outline" value="user">User</v-btn>
          <v-btn prepend-icon="mdi-currency-usd" value="trainer">Trainer</v-btn>
          <v-btn prepend-icon="mdi-gavel" value="admin">Admin</v-btn>
        </v-btn-toggle>
      </v-col>
      <Error v-if="errorOccured" text="Invalid input" />
      <v-btn @click="signUp(creds)" class="mb-8" color="green" size="large" variant="tonal" block
        >Sign Up</v-btn
      >
    </v-card>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import type { Ref } from 'vue'
import type { RegisterCreds } from '../types/credentials'
import { postSignup } from '@/requests/auth'
import Error from './ErrorComponent.vue'

const creds: Ref<RegisterCreds> = ref<RegisterCreds>({
  password: '',
  email: '',
  username: '',
  role: 'user'
})

const emit = defineEmits<{
  signup: string[]
}>()

const errorOccured = ref(false)

const signUp = async (creds: RegisterCreds) => {
  errorOccured.value = false
  try {
    const response = await postSignup(creds)
    emit('signup', creds.username)
  } catch (err) {
    errorOccured.value = true
    console.error(err)
  }
}

const passwordVisible = ref(false)
</script>
