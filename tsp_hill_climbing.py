import random

def distance(city1, city2):
    return ((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)**0.5

def objective_function(path, cities):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distance(cities[path[i]], cities[path[i+1]])
    total_distance += distance(cities[path[-1]], cities[path[0]])
    return total_distance

# define the hill climbing algorithm
def hill_climbing_tsp(cities, max_iter):
    path = list(range(len(cities)))
    random.shuffle(path)
    
    for i in range(max_iter):
        current_value = objective_function(path, cities)
        
        neighborhood = []
        for i in range(len(path)):
            for j in range(i+1, len(path)):
                new_path = path.copy()
                new_path[i], new_path[j] = new_path[j], new_path[i]
                neighborhood.append(new_path)
        
        neighborhood_values = [objective_function(p, cities) for p in neighborhood]
        
        best_value = min(neighborhood_values)
        best_index = neighborhood_values.index(best_value)
        best_path = neighborhood[best_index]
        
        if best_value < current_value:
            path = best_path
    
    return path

cities = [(0, 0), (1, 2), (3, 1), (2, 5), (4, 4)]
max_iter = 100
best_path = hill_climbing_tsp(cities, max_iter)
print("Best path found:", best_path)
print("Total distance:%.3f" %(objective_function(best_path, cities)),"units")
