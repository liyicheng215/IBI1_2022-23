"""
at first rabbit number is n = 2 and the generation = 1
while n <= 100 n*2 and generation+1 (loop until n > 100)
print of value of generation
"""
n = 2
generation = 1
while n <= 100:
    n *= 2  # Each generation, the number of rabbits doubles
    generation += 1  # Each generation, generation plus 1
print(generation)
