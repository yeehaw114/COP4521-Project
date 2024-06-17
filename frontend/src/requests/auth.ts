import type { LoginCreds, RegisterCreds } from '@/types/credentials'
import type { User } from '@/types/user'
import { SERV_NAME } from '@/requests/host'
import { useUserStore } from '@/stores/user'

type authResponse = {
  access: string
  refresh: string
  user: User
}

type refreshRequest = {
  refresh: string
}

type refreshResponse = {
  access: string
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
      localStorage.setItem('refresh-token', data.refresh)
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
      localStorage.setItem('refresh-token', data.refresh)
      const userStore = useUserStore()
      userStore.user = data.user
      userStore.isLoggedIn = true
    })
}

export async function tokenLogin() {
  if (!localStorage.getItem('refresh-token')) {
    return
  }
  const token = localStorage.getItem('refresh-token')
  const refresh: refreshRequest = {
    refresh: token ?? ''
  }
  await fetch(SERV_NAME + '/api/auth/refresh/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(refresh)
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error(response.statusText)
      }
      return response.json()
    })
    .then((data: refreshResponse) => {
      localStorage.setItem('jwt-token', data.access)
      const userStore = useUserStore()
      // userStore.user = data.user
      userStore.isLoggedIn = true
    })
}
