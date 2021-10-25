import pandas as pd

tsp = pd.read_csv("Data/tsp1.csv", index_col=0)

print(tsp)

def pointDistance(x1, y1, x2, y2):
    distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
    return distance


# Loops though each city (row) 
# Can use distance function to find minimum distance between each city
for i in range(0, tsp.shape[0]):
    city = tsp.iloc[i]

    print(city)