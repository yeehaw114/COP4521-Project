import { ref } from 'vue'
import type { Ref } from 'vue'
import { defineStore } from 'pinia'
import type { User } from '../types/user'

export const useUserStore = defineStore('user', () => {
  const user: Ref<User> = ref({
    username: '',
    email: '',
    id: 0
  })
  const isLoggedIn = ref(false)

  return { isLoggedIn, user }
})
