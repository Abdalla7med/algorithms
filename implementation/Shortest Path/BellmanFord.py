class Edge:
    def __init__(self, From, to, Weight):
        self.From=From
        self.To=to
        self.Weight=Weight
"""
The running time of algorithm is O(|V||E|) which is n^2 best case 
and n^3 worst case when graph is dense 
the bellmanford algorithm when Dijkstra's fails to find SSSP
because Dijkstra's doesn't work with negative edge weight graphs 
"""
def BellmanFord(G, v, S):

    dist=[float("inf")]*len(G)
    parent=[None]*len(G)
    dist[S]=0
    for i in range(v):
        for edges in G:
            for edge in edges:
                if dist[edge.To] > dist[edge.From]+edge.Weight:
                    dist[edge.To]=dist[edge.From]+edge.Weight
        
    # run the algorithm for the second time to detect vertex that is a part of negative edge cycle 
    for i in range(v):
        for edges in G:
            for edge in edges:
                if dist[edge.To] > dist[edge.From]+edge.Weight:
                    dist[edge.To]=float("inf")
    
    return dist

# Adj list 
graph=[[] for _ in range(10)]

v,start=9,0
graph[0].append(Edge(0, 1, 1))
graph[1].append(Edge(1, 2, 1))
graph[2].append(Edge(2, 4, 1))
graph[4].append(Edge(4, 3, -3))
graph[3].append(Edge(3, 2, 1))
graph[1].append(Edge(1, 5, 4))
graph[1].append(Edge(1, 6, 4))
graph[5].append(Edge(5, 6, 5))
graph[6].append(Edge(6, 7, 4))
graph[5].append(Edge(5, 7, 3))


dist=BellmanFord(graph,v,start)

for i in range(v):
    print(f"distance form {start} to {i} is {dist[i]}") \
        if dist[i]!=float("inf") else print(f"there's a Negative Edge Cycle Between {start} and {i}")