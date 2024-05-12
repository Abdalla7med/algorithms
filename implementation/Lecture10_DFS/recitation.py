
"""

Depth First Search Algorithm 
Running Time is O(V+E)
like Breadth Frist Search 

"""
Adj={
    0:{1,3,4},
    1:{0,2,5},
    2:{1,3,4},
    3:{0,2},
    4:{1,2},
    5:{1}
}
 # 3 -> 0 -> 1-> 2 -> 4 ->( we return to 1 and then 5 is printed )


# Recursive Depth First Search 
Visited=set()

def dfs(Adj,s):
    Visited.add(s)
    for v in Adj[s]:
        if v not in Visited:
            print(v)
            dfs(Adj,v)

parent={}
"""
to achieve higher performance instead of use call stack we 
 build our own stack 
 also is O(V+E)
"""

def DFS(Adj,s):
    stack=[s]

    while stack:
        u = stack.pop()
        if u not in Visited:
            Visited.append(u)
            for v in Adj[u]:
                if v not in Visited:
                    stack.append(v)

    return Visited

def dfs_pre(Adj,s):
    Visited.add(s)
    for v in Adj[s]:
        if v not in Visited:
            print(v)
            dfs(Adj,v)

            
def dfs_post(Adj,s):
    Visited.add(s)
    for v in Adj[s]:
        if v not in Visited:
            dfs(Adj,v)
            print(v)
"""
Difference between Preorder and Postorder DFS
the only different thing that
 we visit current node firstly after its neightbours in preorder
in postorder we visit neighbours first then current node 
"""
"""dfs(Adj,3)
print(DFS(Adj,3))
"""

print("preorder DFS")
dfs_pre(Adj,3)
print("postder DFS")
dfs_post(Adj,3)
