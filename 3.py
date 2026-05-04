import heapq

def a_star(graph, start, goal, heuristic):
    open_list = []
    heapq.heappush(open_list, (0, start))
    
    g_cost = {start: 0}
    parent = {start: None}
    
    while open_list:
        current_f, current = heapq.heappop(open_list)
        
        if current == goal:
            # reconstruct path
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]
        
        for neighbor, cost in graph[current]:
            new_g = g_cost[current] + cost
            
            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                f = new_g + heuristic[neighbor]
                
                heapq.heappush(open_list, (f, neighbor))
                parent[neighbor] = current
    
    return None


# Graph (node: [(neighbor, cost)])
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 3), ('C', 2)],
    'C': [('D', 1)],
    'D': []
}

# Heuristic values (estimate to goal D)
heuristic = {
    'A': 3,
    'B': 2,
    'C': 1,
    'D': 0
}

path = a_star(graph, 'A', 'D', heuristic)

print("Shortest Path:", path)