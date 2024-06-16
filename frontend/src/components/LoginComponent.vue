<template>
  <div>
    <v-card class="mx-auto pa-12" elevation="10" max-width="450" rounded="lg">
      <div class="text-subtitle-1 text-medium-emphasis">Email</div>
      <v-text-field
        v-model="creds.email"
        density="compact"
        placeholder="Email"
        prepend-inner-icon="mdi-email-outline"
        variant="outlined"
      ></v-text-field>
      <div class="text-subtitle-1 text-medium-emphasis">Password</div>
      <v-text-field
        v-model="creds.password"
        :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
        :type="visible ? 'text' : 'password'"
        density="compact"
        placeholder="Enter your password"
        prepend-inner-icon="mdi-lock-outline"
        variant="outlined"
        @click:append-inner="visible = !visible"
      ></v-text-field>
      <Error v-if="errorOccured" text="Invalid credentials." />
      <v-btn @click="login(creds)" class="mb-8" color="green" size="large" variant="tonal" block
        >Login</v-btn
      >
    </v-card>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import type { Ref } from 'vue'
import type { LoginCreds } from '../types/credentials'
import { postLogin } from '@/requests/auth'
import Error from './ErrorComponent.vue'

const emit = defineEmits<{
  login: string[]
}>()

const creds: Ref<LoginCreds> = ref<LoginCreds>({
  password: '',
  email: ''
})
const errorOccured = ref(false)

const login = async (creds: LoginCreds) => {
  errorOccured.value = false
  try {
    const response = await postLogin(creds)
    emit('login', creds.email)
  } catch (err) {
    errorOccured.value = true
    console.log(err)
  }
}

const visible = ref(false)
</script>
