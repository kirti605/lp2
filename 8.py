import heapq

def dijkstra(graph, start):
    pq = [(0, start)]   # (distance, node)
    dist = {node: float('inf') for node in graph}
    dist[start] = 0

    parent = {start: None}

    while pq:
        current_dist, node = heapq.heappop(pq)

        for neighbor, weight in graph[node]:
            new_dist = current_dist + weight

            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                parent[neighbor] = node
                heapq.heappush(pq, (new_dist, neighbor))

    return dist, parent


# Graph
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('C', 1), ('D', 7)],
    'C': [('D', 3)],
    'D': []
}

dist, parent = dijkstra(graph, 'A')

print("Shortest distances:", dist)