import { ref } from 'vue'
import type { Ref } from 'vue'
import { defineStore } from 'pinia'
import type { User } from '../types/user'

export const useUserStore = defineStore('user', () => {
  const user: Ref<User | null> = ref(null)
  const isLoggedIn = false

  return { isLoggedIn, user }
})
