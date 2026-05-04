class DisjointSet:
    def __init__(self, vertices):
        self.parent = {}
        
        for v in vertices:
            self.parent[v] = v

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])  # Path compression
        return self.parent[node]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            self.parent[root_v] = root_u


def kruskal(vertices, edges):
    # Step 1: Sort edges by weight
    edges.sort(key=lambda x: x[2])

    ds = DisjointSet(vertices)
    mst = []

    # Step 2: Process edges
    for u, v, weight in edges:
        if ds.find(u) != ds.find(v):
            mst.append((u, v, weight))
            ds.union(u, v)

    return mst


# Example graph
vertices = ['A', 'B', 'C', 'D']

edges = [
    ('A', 'B', 1),
    ('A', 'C', 3),
    ('B', 'C', 2),
    ('C', 'D', 4)
]

mst = kruskal(vertices, edges)

print("Minimum Spanning Tree:")
for u, v, w in mst:
    print(f"{u} - {v} = {w}")