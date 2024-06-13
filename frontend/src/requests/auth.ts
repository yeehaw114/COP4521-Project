import type { LoginCreds, RegisterCreds } from '@/types/credentials'
import type { User } from '@/types/user'
import { SERV_NAME } from '@/ts/host'
import { useUserStore } from '@/stores/user'

type authResponse = {
  access: string
  refresh: string
  user: User
}

export async function postSignup(creds: RegisterCreds) {
  await fetch(SERV_NAME + '/api/auth/register/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(creds)
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error(response.statusText)
      }
      return response.json()
    })
    .then((data: authResponse) => {
      localStorage.setItem('jwt-token', data.access)
      const userStore = useUserStore()
      userStore.user = data.user
      userStore.isLoggedIn = true
      return data
    })
}

export async function postLogin(creds: LoginCreds) {
  await fetch(SERV_NAME + '/api/auth/login/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(creds)
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error(response.statusText)
      }
      return response.json()
    })
    .then((data: authResponse) => {
      localStorage.setItem('jwt-token', data.access)
      const userStore = useUserStore()
      userStore.user = data.user
      userStore.isLoggedIn = true
    })
}
