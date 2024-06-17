export type Workout = {
  name: string
  sets: Set[]
}

export type CreateWorkoutu = {
  name: string
  sets: Set[]
}

export type Set = {
  exercise: string
  reps: number
  weight: number
}

export type CreateSet = {
  exercisie: string
  reps: number
  weight: number
}

export type Exercise = {
  name: string
  sets: Set[]
}
