export type Workout = {
  name: string
  id: number
  sets: Set[]
}

export type CreateWorkout = {
  name: string
  sets: Set[]
}

export type Set = {
  exercise: string
  id: number
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

export type MiniLog = {
  id: number
  workout_id: number
  done_date: Date
  username: string
}

export type MiniWorkout = {
  id: number
  name: string
}

export function convertSetsToExercises(sets: Set[]): Exercise[] {
  const exerciseMap: Map<string, Exercise> = sets.reduce((map, set) => {
    if (!map.has(set.exercise)) {
      map.set(set.exercise, { name: set.exercise, sets: [] })
    }
    map
      .get(set.exercise)
      ?.sets.push({ exercise: set.exercise, id: set.id, reps: set.reps, weight: set.weight })
    return map
  }, new Map<string, Exercise>())
  return Array.from(exerciseMap.values()) as Exercise[]
}

export function convertExercisesToSets(exercises: Exercise[]): Set[] {
  let sets: Set[] = []
  for (let e of exercises) {
    for (let s of e.sets) {
      sets.push(JSON.parse(JSON.stringify(s)))
    }
  }
  return sets
}
