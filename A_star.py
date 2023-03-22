import heapq

graph = {
    'A': {'B': 2, 'C': 5},
    'B': {'D': 3, 'E': 1},
    'C': {'F': 7},
    'D': {'F': 2},
    'E': {'F': 4},
    'F': {}
}

heuristic = {
    'A': 8,
    'B': 6,
    'C': 7,
    'D': 2,
    'E': 4,
    'F': 0
}

def a_star(start, goal):
    frontier = [(0, start)]
    came_from = {}
    cost_so_far = {start: 0}

    while frontier:
        current_cost, current_node = heapq.heappop(frontier)

        if current_node == goal:
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start)
            path.reverse()
            return path

        for neighbor, cost in graph[current_node].items():
            new_cost = cost_so_far[current_node] + cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]
                heapq.heappush(frontier, (priority, neighbor))
                came_from[neighbor] = current_node

    return None

path = a_star('A', 'F')
print(path)
