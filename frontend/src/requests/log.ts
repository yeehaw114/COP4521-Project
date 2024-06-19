import { SERV_NAME } from '@/requests/host'
import type { Workout, Set, MiniLog } from '@/types/workout'

export async function getLog(id: number): Promise<Workout> {
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
    .then((data: Workout) => {
      console.log(data)
      return data
    })
}

export async function postLog(workout: Workout) {
  const token = localStorage.getItem('jwt-token')
  console.log(JSON.stringify(workout))
  return await fetch(SERV_NAME + '/api/workouts/' + workout.id + '/log-workout/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${token}`
    },
    body: JSON.stringify(workout)
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
