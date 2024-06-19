import { SERV_NAME } from '@/requests/host'
import type { Workout, Set, MiniLog, Log } from '@/types/workout'

export async function getLog(id: number): Promise<Log> {
  const token = localStorage.getItem('jwt-token')
  return await fetch(SERV_NAME + '/api/workouts/' + id + '/log/', {
    method: 'GET',
    headers: {
      Authorization: `Bearer ${token}`
    }
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error(response.statusText)
      }
      return response.json()
    })
    .then((data: Log) => {
      console.log(data)
      return data
    })
}

const replacer = (key: any, value: any) => {
  if (key === 'id') {
    return undefined
  }
  return value
}

export async function postLog(workoutid: number, s: Set[]) {
  const req = {
    sets: s
  }
  const token = localStorage.getItem('jwt-token')
  return await fetch(SERV_NAME + '/api/workouts/' + workoutid + '/log-workout/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${token}`
    },
    body: JSON.stringify(req)
  }).then((response) => {
    if (!response.ok) {
      throw new Error(response.statusText)
    }
    return response.json()
  })
}

export async function deleteLog(id: number) {
  const token = localStorage.getItem('jwt-token')
  return await fetch(SERV_NAME + '/api/workouts/' + id + '/delete-log/', {
    method: 'DELETE',
    headers: {
      Authorization: `Bearer ${token}`
    }
  }).then((response) => {
    if (!response.ok) {
      throw new Error(response.statusText)
    }
    return response.json()
  })
}

export async function getUserLogs(): Promise<MiniLog[]> {
  const token = localStorage.getItem('jwt-token')
  return await fetch(SERV_NAME + '/api/user-workouts/logs/', {
    method: 'GET',
    headers: {
      Authorization: `Bearer ${token}`
    }
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error(response.statusText)
      }
      return response.json()
    })
    .then((data: MiniLog[]) => {
      return data
    })
}

export async function updateLog(logid: number, logSets: Set[]) {
  const token = localStorage.getItem('jwt-token')
  const req = {
    sets: logSets
  }
  console.log(JSON.stringify(req))
  return await fetch(SERV_NAME + '/api/workouts/' + logid + '/update-log/', {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${token}`
    },
    body: JSON.stringify(req)
  }).then((response) => {
    if (!response.ok) {
      throw new Error(response.statusText)
    }
    return response.json()
  })
}
