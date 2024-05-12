class DisjointSet:
    def __init__(self,n) -> None:
        self.parent=[n]
        self.rank=[n]
    
    def FindParent(self,node):
        if node==self.parent[node]:
            return node
        self.parent[node]=self.FindParent(self.parent[node])
        return self.parent[node]

    def UnionByRank(self,U,V):
        Up=self.FindParent(U,V)
        Vp=self.FindParent(U,V)
        if Up==Vp:
            return 
        if self.rank[Up]<self.rank[Vp]:
            self.parent[Up]=Vp
        elif self.rank[Vp]<self.rank[Up]:
            self.parent[Vp]=Up
        else:
            self.parent[Up]=Vp
            self.rank[Vp]+=1




