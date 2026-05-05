from collections import deque

def bfs(graph,start):
    visited = set()
    queue = deque()

    visited.add(start)
    queue.append(start)

    while queue:
        node = queue.popleft()
        print(node,end=" ")

        for x in graph[node]:
            if x not in visited:
                visited.add(x)
                queue.append(x)

graph={
    'A' :['B','C'],
    'B' :['A','D'],
    'C' :['A','D'],
    'D' :['B','C']
}

bfs(graph,'A')
 //Recursive style
from collections import deque

def bfs_recursive(queue, visited, graph):
    if not queue:
        return
    
    node = queue.popleft()
    print(node, end=" ")
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
    
    bfs_recursive(queue, visited, graph)


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

visited = set(['A'])
queue = deque(['A'])

bfs_recursive(queue, visited, graph)


