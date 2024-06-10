

class Set:
    reps:int
    weight:int

class Exercise:
    name:str
    sets: [Set]

class Workout:
    name:str
    exercises: [Exercise]