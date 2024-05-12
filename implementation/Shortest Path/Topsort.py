
class Edge:
    def __init__(self,From,To,Weight):
        From=From
        To=To
        Weight=Weight

def Topsort(graph:list[list[int]]):
    N=len(graph)
    v=[False for i in range(N)]
    ordering=[0]*N
    i=N-1
    def dfs(i, v, at,ordering, graph):
        v[at]=True

        Adj=graph[at]

        for node in Adj:
            if v[node]==False:
                i=dfs(i, node, v, ordering, graph)
        ordering[i]=at
        return i-1
    for at in range(N):
        i=dfs(i, at, v, ordering, graph)
    return ordering

    

#Example of usage

graph=[[] for _ in range(6)]


graph[0].append(1)
graph[0].append(2)
graph[0].append(5)
graph[1].append(3)
graph[1].append(2)
graph[2].append(3)
graph[2].append(4)
graph[3].append(4)
graph[5].append(4)
print(Topsort(graph))



