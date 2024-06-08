import type { LoginCreds, RegisterCreds } from "@/types/credentials";
import { SERV_NAME } from '@/ts/host'
export function postSignup(creds:RegisterCreds) {
    fetch(SERV_NAME+'/api/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(creds) 
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(response.statusText)
        }
        return response.json()
    })
    .then(data => {
        console.log("signup successful:", data)
    })
    .catch(e => {
        console.error(e)
    })
}

export function postLogin(creds:LoginCreds) {
    fetch(SERV_NAME+'/api/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(creds) 
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(response.statusText)
        }
        return response.json()
    })
    .then(data => {
        console.log("login successful:", data)
    })
    .catch(e => {
        console.error(e)
    })
}