graph = {
    'A': ['B', 'C','E'],
    'B': ['D', 'E'],
    'C': ['F','D'],
    'D': ['E'],
    'E': ['F'],
    'F': []
}

def idft(graph, start):
    stack = [start]
    visited = set()
    
    while stack:
        node = stack.pop()
        
        if node not in visited:
            visited.add(node)
            print(node,"-->", end=' ')
            for neighbor in graph[node]:
                stack.append(neighbor)

idft(graph, 'A')
