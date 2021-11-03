import pandas as pd
import random
import pygad
from datetime import datetime

file = input("Enter file path: ")
tsp = pd.read_csv(file, index_col=0)

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
def fitness(solution, solution_idx):
    totalDistance = 0
    
    firstCity = [0,0]
    firstCityx = firstCity.pop(0)
    firstCityy = firstCity.pop(0)

    for i in range(len(solution) - 1):
        city = tsp.loc[solution[i]]
        city2 = tsp.loc[solution[i+1]]
        totalDistance += pointDistance(city.loc["x"],city.loc["y"],city2.loc["x"],city2.loc["y"])
    
    lastCity = tsp.loc[solution[i+1]]
    
    totalDistance += pointDistance(firstCityx,firstCityy,lastCity.loc["x"],lastCity.loc["y"])

    

# Return inverse of distance
# Small distance is high fitness
# Alternative could be -1 * totalDistance
    return 1/totalDistance

# The on_generation is a function that will be called at the end of each generation. 
# In this case we will print out the gen number. 

def on_generation(g):
    print(datetime.now(), "Gen", g.generations_completed)
    # print("Best Solution", captures(ga_instance.best_solution(),1))
    #for p in ga.population:
       # print(p, captures(p,1)) 

# run the ga. 
def ga(): 
    print("Number of cities: ", numRows)
    # set up the parameters 
    
    # assign the fitness function
    fitness_function = fitness
    
    # how many generations to run for? 
    num_generations = 100

    # what is the population size? 
    sol_per_pop = 100

    # Set up the genes. How many genes make up an individual and what are the values that 
    # each gene can take on. 
    # In this example there are 8 genes, each representing a column on the chessboard, and 
    # that possible values are 1-8 for which row the queen is placed. 

    num_genes = numRows
    gene_space = range(1, numRows + 1)
    #init_range_low = 1
    #init_range_high = 8

    # Then we need to control how the various genetic operators are applied. 
    num_parents_mating = 2
    parent_selection_type = "sss"
    keep_parents = 1

    crossover_type = "single_point"

    mutation_type = "random"
    mutation_percent_genes = 1
    
    ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_function,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       #init_range_low=init_range_low,
                       #init_range_high=init_range_high,
                       parent_selection_type=parent_selection_type,
                       keep_parents=keep_parents,
                       crossover_type=crossover_type,
                       mutation_type=mutation_type,
                       mutation_percent_genes=mutation_percent_genes,
                       gene_space=gene_space,
                       allow_duplicate_genes=False,
                       on_generation=on_generation)
    ga_instance.run()
    
    ga_instance.plot_fitness()
    
    s, fit, s_i = ga_instance.best_solution()
    print(s)
    return s


sol = ga()