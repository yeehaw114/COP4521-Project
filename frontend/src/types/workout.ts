export type Workout = {
  name: string
  sets: Set[]
  id:number
}

export type Set = {
  exercise: string
  reps: number
  weight: number
  id:number
}

export type Exercise = {
  name: string
  sets: Set[]
}
