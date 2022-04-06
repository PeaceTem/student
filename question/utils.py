import random



def randomQuestions(value: list, size: str):
     goal = random.choices(value, k=size)
     return goal
