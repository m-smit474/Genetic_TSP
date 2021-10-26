import pandas as pd
import random

tsp = pd.read_csv("Data/tsp1.csv", index_col=0)

# gets number of rows
numRows = tsp.shape[0]

# Calculates distance between two coordinates
def pointDistance(x1, y1, x2, y2):
    distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
    return distance

# Generates a random solution
def solution():
    sol = []
    for i in range(numRows):
        sol.append(random.randint(1,numRows))
    return sol

# Determines total distance of a given solution
# ** I believe this currently doesn't count the last city
def fitness(solution):
    totalDistance = 0
    for i in range(len(solution) - 1):
        city = tsp.loc[solution[i]]
        city2 = tsp.loc[solution[i+1]]
        totalDistance += pointDistance(city.loc["x"],city.loc["y"],city2.loc["x"],city2.loc["y"])

# Return inverse of distance
# Small distance is high fitness
# Alternative could be -1 * totalDistance
    return 1/totalDistance



# Testing
A = solution()
print(A)
print(fitness(A))

B = solution()
print(B)
print(fitness(B))