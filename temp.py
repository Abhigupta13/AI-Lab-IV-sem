import random

# Define the objective function that we want to optimize
def objective_function(x):
    return x**2

# Define the hill climbing algorithm
def hill_climbing(search_space, max_iterations):
    # Start with a random solution
    current_solution = random.choice(search_space)
    # Evaluate the objective function for the current solution
    current_value = objective_function(current_solution)
    # Keep track of the number of iterations
    iterations = 0
    # Continue iterating until we reach the maximum number of iterations or find the optimal solution
    while iterations < max_iterations:
        # Generate a new solution by making a small incremental change to the current solution
        new_solution = current_solution + random.uniform(-0.1, 0.1)
        # Evaluate the objective function for the new solution
        new_value = objective_function(new_solution)
        # If the new solution is better than the current solution, move to the new solution
        if new_value < current_value:
            current_solution = new_solution
            current_value = new_value
        # Increment the number of iterations
        iterations += 1
    # Return the optimal solution
    return current_solution

# Define the search space
search_space = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

# Call the hill climbing algorithm with a maximum of 100 iterations
optimal_solution = hill_climbing(search_space, 100)

# Print the optimal solution
print("Optimal solution:", optimal_solution)
