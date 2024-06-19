<template>
  <v-navigation-drawer :width="200" :close-delay="200" permanent absolute rail expand-on-hover>
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
    <template v-else>
      <v-list>
        <v-list-item link>
          <UserAvatar />
        </v-list-item>
        <v-list-item prepend-icon="mdi-logout" title="Logout" link @click="logout"></v-list-item>
      </v-list>
      <v-divider></v-divider>
      <v-list>
        <v-list-item
          prepend-icon="mdi-plus-box-outline"
          link
          to="/workout/create"
          title="Create Workout"
        ></v-list-item>
      </v-list>
    </template>
    <v-divider></v-divider>
    <v-list>
      <v-list-item prepend-icon="mdi-home" link to="/" title="Home"></v-list-item>
      <v-list-item prepend-icon="mdi-information" link to="/about" title="About"></v-list-item>
      <v-list-item prepend-icon="mdi-theme-light-dark" link title="Toggle theme" @click="toggleTheme"></v-list-item>
    </v-list>
  </v-navigation-drawer>

  <SuccessSnackbar v-model="successLoginSnackbar" text="Successfully logged in" />
  <SuccessSnackbar v-model="successSignupSnackbar" text="Sucessfully signed up" />

  <v-dialog v-model="signupDialog">
    <Signup @signup="closeSignUpDialog" />
  </v-dialog>

  <v-dialog v-model="loginDialog">
    <Login @login="closeLoginDialog" />
  </v-dialog>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'
import { useUserStore } from '../stores/user'
import { logout } from '@/requests/auth'
import Signup from './SignUp.vue'
import Login from './LoginComponent.vue'
import SuccessSnackbar from './SuccessfulSnackbar.vue'
import UserAvatar from './UserAvatar.vue'
import { useTheme } from 'vuetify'

const successLoginSnackbar = ref(false)
const successSignupSnackbar = ref(false)

const userStore = useUserStore()
const username = ref('')

watch(username, (newUsername) => {
  console.log(`username changed to ${username}`)
  //username.value = newUsername ?? ""
})

const theme = useTheme()

const toggleTheme = () => {
  const isDark = theme.global.current.value.dark
  theme.global.name.value = isDark ? "light" : "dark"
}

const signupDialog = ref(false)
const openSignUpDialog = () => {
  signupDialog.value = true
}
const closeSignUpDialog = () => {
  signupDialog.value = false
  successSignupSnackbar.value = true
}

const loginDialog = ref(false)
const openLoginDialog = () => {
  loginDialog.value = true
}
const closeLoginDialog = () => {
  loginDialog.value = false
  successLoginSnackbar.value = true
}
</script>

<style scoped></style>
