import type { LoginCreds, RegisterCreds } from '@/types/credentials'
import { SERV_NAME } from '@/ts/host'

type getToken = {
  csrfToken:string
}

export async function getToken() {
  await fetch(SERV_NAME + '/auth/csrf-token', {
    method: 'GET'
  })
  .then((response) => {
    if (!response.ok) {
     throw new Error(response.statusText) 
    }
    return response.json()
  })
  .then((data:getToken)=> {
    console.log("data is "+data.csrfToken)
    localStorage.setItem('csrfToken',data.csrfToken)
  })
  .catch((error)=>{
    console.error(`App may not work as expected: ${error}` )
  })
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
      console.log('signup successful:', data)
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
