import heapq;
class Edge:
    def __init__(self, From, to, Weight):
        self.From=From
        self.To=to
        self.Weight=Weight

def dijkstra(g, n, s):
    vis=[False]*n
    dist=[float("inf")]*n
    prev=[None]*n
    dist[s]=0
    pq=[]
    heapq.heappush(pq,(s, 0)) # index , distance

    while pq:
        index,minValue=heapq.heappop(pq)
        vis[index]=True
        for edge in g[index]:
            if vis[edge.To]:
                continue
            newDist=dist[index]+edge.Weight
            if newDist < dist[edge.To]:
                dist[edge.To]=newDist
                prev[edge.To]=index
                heapq.heappush(pq,(edge.To,newDist)) # this will lead to duplicates but pq keep minimum first
    return (dist,prev) # return shortest distance, shortest path 


"""
need to find shortest path from node s to node e 
"""

def ShortestPath(g, n, s, e):
    dist,prev=dijkstra(g, n, s)
    path=[]
    # there's no path exists

    if dist[e]==float("inf"):
        return path # empty path
    
    at=e
    while at!=None:
        path.append((at,dist[at]))
        at=prev[at]

    path.reverse()
    return path

# create graph as node : edges

graph=[[] for _ in range(7)]


graph[0].append(Edge(0, 1, 3))
graph[0].append(Edge(0, 2, 2))
graph[0].append(Edge(0, 5, 3))
graph[1].append(Edge(1, 3, 1))
graph[1].append(Edge(1, 2, 6))
graph[2].append(Edge(2, 4, 10))
graph[2].append(Edge(2, 3, 1))
graph[3].append(Edge(3, 4, 5))
graph[5].append(Edge(5, 4, 7))

print(ShortestPath(graph, 6, 0, 4))


