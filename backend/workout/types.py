from typing import List

class Set:
    def __init__(self, reps:int, weight:int):
        self.reps=reps
        self.weight=weight

class Exercise:
    def __init__(self, name:str, sets:List[Set]):
        self.name=name
        self.sets=sets

class Workout:
    def __init__(self, name:str, exercises:List[Exercise]):
        self.name = name
        self.exercises = exercises