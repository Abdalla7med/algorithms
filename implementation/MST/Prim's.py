import heapq;
class Edge:
    def __init__(self, From, to, Weight):
        self.From=From
        self.To=to
        self.Weight=Weight

def Prims(Adj,n,S):
    MST_Weight=0

    pq=[] # to keep edges
    key=[float("inf")]*n # minimum Weight of edge to vertx 

    visited=[False]*n
    parent=[None]*n

    key[S]=0 # minim Edge cost 
    heapq.heappush(pq,(0,S))
    while pq:
        W,U=heapq.heappop(pq)
        if visited[U]==True:
            continue

        visited[U]=True
        MST_Weight += key[U]

        for Edge in Adj[U]:
            if visited[Edge.To]==False and Edge.Weight < key[Edge.To]:
                
                key[Edge.To]=Edge.Weight
                parent[Edge.To]=Edge.From
                heapq.heappush(pq,(key[Edge.To],Edge.To))


    return MST_Weight

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

print(f"Total Weight of MST is {Prims(graph,v,start)}")





