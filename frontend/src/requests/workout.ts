import { SERV_NAME } from '@/requests/host'
import type { Workout, MiniWorkout } from '@/types/workout'

export async function postWorkout(workout: Workout) {
  const token = localStorage.getItem('jwt-token')
  await fetch(SERV_NAME + '/api/workouts/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${token}`
    },
    body: JSON.stringify(workout)
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error(response.statusText)
      }
      return response.json()
    })
    .then((data) => {
      return data
    })
}

export async function getWorkout(id: number): Promise<Workout> {
  const token = localStorage.getItem('jwt-token')
  return await fetch(SERV_NAME + '/api/workouts/' + id + '/details/', {
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

export async function getUserWorkouts():Promise<MiniWorkout[]> {
  const token = localStorage.getItem('jwt-token')
  return await fetch(SERV_NAME+'/api/workouts/user-workouts/', {
    method: 'GET',
    headers: {
      Authorization: `Bearer ${token}`
    }
  })
  .then((response) => {
    if(!response.ok) {
      throw new Error(response.statusText)
    }
    return response.json()
  })
  .then((data:MiniWorkout[]) => {
    return data
  })
}

export async function deleteWorkout(id: number) {
  const token = localStorage.getItem('jwt-token')
  await fetch(SERV_NAME + '/api/workouts/' + id + '/', {
    method: 'GET',
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
