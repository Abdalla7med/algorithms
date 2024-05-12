import heapq
# class Graph():
#    INF = 999999
#    def __init__(self, num_vertices):
#        self.V = num_vertices
#        self.graph = [[0 for column in range(num_vertices)] for row in range(num_vertices)]
      
#    # pretty print of the minimum spanning tree
#    # prints the MST stored in the list var `parent`
#    def printMST(self, parent):
#        print("Edge     Weight")
#        for i in range(1, self.V):
#            print(f"{parent[i]} - {i}       {self.graph[i][parent[i]]}")
  
#    # finds the vertex with the minimum distance value
#    # takes a key and the current set of nodes in the MST
#    def minKey(self, key, mstSet):
#        min = self.INF
#        for v in range(self.V):
#            if key[v] < min and mstSet[v] == False:
#                min = key[v]
#                min_index = v
#        return min_index
  
#    # prim's algo, graph is represented as an v by v adjacency list
#    def prims(self):
#        # used to pick minimum weight edge
#        key = [self.INF for _ in range(self.V)]
#        # used to store MST
#        parent = [None for _ in range(self.V)]
#        # pick a random vertex, ie 0
#        key[0] = 0
#        # create list for t/f if a node is connected to the MST
#        mstSet = [False for _ in range(self.V)]
#         # set the first node to the root (ie have a parent of -1)
#        parent[0] = -1
 
#        for _ in range(self.V):
#            # 1) pick the minimum distance vertex from the current key
#            # from the set of points not yet in the MST
#            u = self.minKey(key, mstSet)
#            # 2) add the new vertex to the MST
#            mstSet[u] = True
 
#            # loop through the vertices to update the ones that are still
#            # not in the MST
#            for v in range(self.V):
#                # if the edge from the newly added vertex (v) exists,
#                # the vertex hasn't been added to the MST, and
#                # the new vertex's distance to the graph is greater than the distance
#                # stored in the initial graph, update the "key" value to the
#                # distance initially given and update the parent of
#                # of the vertex (v) to the newly added vertex (u)
#                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
#                    key[v] = self.graph[u][v]
#                    parent[v] = u
 
#        self.printMST(parent)




def PrimsSimple (points: list[list[int]]):
    N=len(points)

    Adj={i:[] for i in range(N)}

    for i in range(N):
        x1,y1=points[i]
        for j in range(i+1,N):
            x2,y2=points[j]
            # determine cost of edge 

            dist=abs(x1-x2)+abs(y1-y2)
            # as unidericted graph (i,j) and (j,i) has the same cost 
            Adj[i].append([dist,j])
            Adj[j].append([dist,i])
    #prim's

    res=0
    visit=set()
    MinH=[[0,0]] #minheap
    
    while len(visit) <N:
        cost,i=heapq.heappop(MinH)
        if i in visit:
            continue
        # add cost of MST 

        res+=cost
        visit.add(i)

        # search neighbours 

        for neiCost,nei in Adj[i]:
            if nei not in visit:
                heapq.heappush(MinH,[neiCost,nei])
    return res



def prims_priority_q(graph, start):
    # establish the necessary data structures 
    edges = []
    weights = []
    visited_vertices = [start]

    # terminate when visit all nodes 
    while len(visited_vertices) < len(graph):

        moves = []
        for x in visited_vertices:

            # search neighbours 
            for node in graph[x]:
                # push weight, cur vertex, next vertex
                # could be prettier if we used objects instead
                # of tuples
                if node[0] not in visited_vertices:
                    heapq.heappush(moves, (node[1], x, node[0]))
        
        # get the next move based on the weight
        next_move = heapq.heappop(moves)
        print(f"next move: {next_move}")
        # add the next vertex, total weight, and append the edge
        visited_vertices.append(next_move[2])
        weights.append(next_move[0])
        edges.append((next_move[1], next_move[2]))

    return edges, weights
adj_list_graph=[[(1, 2), (3, 6)],
                [(0, 2), (2, 3), (3, 8), (4, 5)],
                [(1, 3), (4, 7)],
                [(0, 6), (1, 8), (4, 9)],
                [(1, 5), (2, 7), (3, 9)]]

edges, weights = prims_priority_q(adj_list_graph, 0)

print("edges    weights")
for edge, weight in zip(edges, weights):
    print(f"{edge}      {weight}")

