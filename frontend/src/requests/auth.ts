import type { LoginCreds, RegisterCreds } from "@/types/credentials";
import { SERV_NAME } from '@/ts/host'
export function postSignup(creds:RegisterCreds) {
    fetch(SERV_NAME+'register/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(creds) 
    })
}

export function postLogin(creds:LoginCreds) {
    fetch(SERV_NAME+'login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(creds) 
    })
}