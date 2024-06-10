import type { LoginCreds, RegisterCreds } from '@/types/credentials'
import { SERV_NAME } from '@/ts/host'

export async function getToken() {
  await fetch(SERV_NAME + '/api/csrf-token', {
    method: 'GET'
  })
  .then((response) => {
    if (!response.ok) {
     throw new Error(response.statusText) 
    }
  })
  .then((data)=> {
    console.log(data)
    //localStorage.setItem('csrf-token',data)
  })
  .catch((error)=>{
    console.error(`App may not work as expected: ${error}` )
  })
}

export async function postSignup(creds: RegisterCreds) {
  await fetch(SERV_NAME + '/api/register', {
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
      console.log('signup successful:', data)
    })
}

export async function postLogin(creds: LoginCreds) {
  await fetch(SERV_NAME + '/api/login', {
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
