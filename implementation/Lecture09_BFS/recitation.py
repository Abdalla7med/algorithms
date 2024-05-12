
from collections import defaultdict, deque

#First graph 
G1=    {0:{1},
        1:{2},
        2:{0},
        3:{4}}

#second graph
G2={
    0:{1,3,4},
    1:{0},
    2:{3},
    3:{0,2},
    4:{0} }

def BFS(Adj,s):

    parent=[None for v in Adj]
    parent[s]=s

    level=[[s]]
    # not empty 
    while 0 < len(level[-1]):
        level.append([])
        # pop from the queue 
        for u in level[-2]:
            print(u)
            # visit neightbours
            for v in Adj[u]:
                # unvisited vertices 
                if parent[v] is None:
                    parent[v]=u
                    level[-1].append(v)
    return parent

def bfs(graph, start):
    # mark visited nodes 
    visited = set()
    queue = deque([start])
    visited.add(start)

    # not empty case 
    while queue:
        # first vertex in the queue
        vertex = queue.popleft()
        print(vertex, end=' ')

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)


def unweighted_shortest_path(Adj,s,t):
    parent=BFS(Adj,s)
    if parent[t] is None:
        return None
    i=t
    path=[t]
    while i!=s:
        i=parent[i]
        path.append(i)
    return path[::-1]

print(bfs(G2,2))

path=unweighted_shortest_path(G2,1,0)
print("shortest path from 1 to 0 is : ")
print(path) if path is not None else print("path is empty")