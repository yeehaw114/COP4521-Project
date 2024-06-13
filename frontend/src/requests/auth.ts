import type { LoginCreds, RegisterCreds } from '@/types/credentials'
import type { User } from '@/types/user'
import { SERV_NAME } from '@/ts/host'

type postSignupResponse = {
  access:string
  refresh:string
  user:User
}

export async function postSignup(creds: RegisterCreds) {
  await fetch(SERV_NAME + '/auth/register', {
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
    .then((data) => {
      const res:postSignupResponse = JSON.parse(data)
      return res
    })
}

export async function postLogin(creds: LoginCreds) {
  await fetch(SERV_NAME + '/auth/login', {
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
    .then((data) => {
      console.log('login successful:', data)
    })
}
