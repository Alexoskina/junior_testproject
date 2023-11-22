import random

def sixes(num_cubes):
    rolls = [random.randint(1, 6) for _ in range(num_cubes)]
    count = rolls.count(6)
    return count


#example
num_cubes = 5
result = sixes(num_cubes)
print(f"Выпало шестерок из {num_cubes} кубиков: {result}")