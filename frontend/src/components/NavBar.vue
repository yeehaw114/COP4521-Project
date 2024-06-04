<template>
  <v-navigation-drawer :width="200" :close-delay="200" absolute rail expand-on-hover>
    <v-list v-if="!userStore.isLoggedIn">
      <v-list-item
        prepend-icon="mdi-login"
        @click="openLoginDialog"
        link
        title="Login"
      ></v-list-item>
      <v-list-item
        prepend-icon="mdi-account-plus"
        @click="openSignUpDialog"
        link
        title="Signup"
      ></v-list-item>
    </v-list>
    <v-list v-else>
      <v-list-item prepend-icon="mdi-dumbbell" link :title="config.appTitle"></v-list-item>
    </v-list>
    <v-divider></v-divider>
    <v-list>
      <v-list-item prepend-icon="mdi-home" link to="/" title="Home"></v-list-item>
      <v-list-item prepend-icon="mdi-information" link to="/about" title="About"></v-list-item>
    </v-list>
  </v-navigation-drawer>

  <v-dialog v-model="signupDialog">
      <Signup />
  </v-dialog>

  <v-dialog v-model="loginDialog">
      <Login />
  </v-dialog>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import config from '../../config.json'
import { useUserStore } from '../stores/user'
import Signup from './SignUp.vue'
import Login from './LoginComponent.vue'

const userStore = useUserStore()

const signupDialog = ref(false)
const openSignUpDialog = () => {
  signupDialog.value = true
}

const loginDialog = ref(false)
const openLoginDialog = () => {
  loginDialog.value = true
}
</script>

<style scoped></style>
