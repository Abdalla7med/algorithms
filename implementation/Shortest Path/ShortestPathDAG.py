import Topsort
class Edge:
    def __init__(self,From,To,Weight):
        self.From=From
        self.To=To
        self.Weight=Weight


def ShortestPathDAG(G,S):
    topsort=Topsort(G)
    N=len(G)
    dist=[float("inf")]*N
    dist[S]=0
    for i in range(N):

        VertexIndex=topsort[i]

        AdjEdges=G[VertexIndex]
        if AdjEdges:
            for edge in AdjEdges:
               # Relaxation step   
                newDist=dist[VertexIndex]+edge.Weight
                # distance between this Vertex and this doesn't changed 
                if dist[edge.To] ==float("inf"):
                    dist[edge.To]=newDist
                else :
                    dist[edge.To]=min(dist[edge.To], newDist)
    return dist 


"""

@Important : all SSSP algorithms do Edge Relaxation which invloves 
update edege weight by the smallest weight also leading to the same Vertices

@Explaination :
the key difference between other Algos wih SSSP 
and the one used with DAG ?
is that the edges is sorted first in the Ascending order 
and then do the same routine as Dijkstra's algorithm 

Hope this be helpful

"""

# if you wanna try the code add the same Block in the BellmanFord and run it out
