import heapq

def prims(graph,start):
    visited =set()
    minHeap = [(0,start,None)]

    totalCost =0;
    ms=[]

    while minHeap:
        weight,node,parent = heapq.heappop(minHeap)
        if node not in visited:
            visited.add(node)
            totalCost+=weight

            if weight!=0:
                ms.append((parent,node,weight))
            
            for x,cost in graph[node]:
                if x not in visited:
                    heapq.heappush(minHeap,(cost,x,node))

    return ms,totalCost


graph = {
    'A':[('B',2),('C',3)],
    'B':[('A', 2), ('C', 1), ('D', 4)],
    'C': [('A', 3), ('B', 1), ('D', 5)],
    'D': [('B', 4), ('C', 5)]
}

mst , cost = prims(graph,'A')
print(mst)
print(cost)
