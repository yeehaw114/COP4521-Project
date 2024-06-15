import { SERV_NAME } from '@/requests/host'
import type { Workout } from '@/types/workout'

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