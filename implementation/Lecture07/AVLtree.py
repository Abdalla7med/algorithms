# first proposed scheme was the AVL Tree (Adelson-Velsky and Landis,1962)

def height(A):
    if A: return A.height
    else : return -1
class TreeNode:
    def __init__(A,x):
        A.item=x
        A.left=None
        A.right=None
        A.height=0
        A.subtree_update()
    def insert(self, x):
        if self.item < x:
            if self.right is None:
                self.right = TreeNode(x)
                self.right.parent = self
            else:
                self.right.insert(x)
        else:
            if self.left is None:
                self.left = TreeNode(x)
                self.left.parent = self
            else:
                self.left.insert(x)

    def subtree_update(A):
        A.height=1+max(height(A.left),height(A.right))


    def skew(A):
        return height(A.right)-height(A.left)
    
    def subtree_iter(A):
        if A.left:
            A.left.subtree_iter()
        print(A.item)
        if A.right:
            A.right.subtree_iter()


    def subtree_first(A):
        if A.left:
            return A.subtree_first()
        else :
            return A
        

    def subtree_last(A):
        if A.right:
            return A.right.subtree_last()
        else:
            return A
    

    def successor(A):
        if A.left:
            return A.left.subtree_first()
        while A.parent and (A is A.parent.right):
            A=A.parent
        return A.parent


    def predecessor(A):
        if A.left :
            return A.left.subtree_last()
        while A.parent and (A is A.parent.left):
            A=A.parent
        return A.parent
    

    def subtree_insert_before(A, B):
        if A.left:
            A=A.left.subtree_last()
            A.right,B.parent=B,A
        else:
            A.left,B.parent= B,A
        A.maintain()


    def subtree_insert_aftre(A,B):
        if A.right:
            A=A.right.subtree_first()
            A.left,B.parent=B,A
        else:
            A.left ,B.parent= B,A
        A.maintain()


    def subtree_delete(A):
        if A.left or A.right:
            if A.left : B=A.predecessor()
            else: 
                B=A.successor()
            A.item,B.item=B.item,A.item
            return B.subtree_delete()
        if A.parent:
            if A.parent.left is A:
                A.parent.left=None
            else:
                A.parent.right=None
            A.maintain()
        return A
    def subtree_right_rotate(D):
        assert D.left
        B,E=D.left,D.right
        A,C=B.left,B.right

        B.left,B.right=A,D
        D.left,D.right=C,E
        if A: A.parent=B
        if E: E.parent=D
        B.subtree_update()
        D.subtree_update()

    def subtree_left_rotate(B):
        # this keyword ensure that B has right child else it will out the code 
        assert B.right
        A,D=B.left,B.right
        C,E=D.left,D.right
        # not necessary but it's to achieve efficient rotations 
        B,D=D,B
        B.item,D.item=D.item,B.item
        D.left,D.right=B,E
        B.left,B.right=A,C
        if A: A.parent=B
        if E: E.parent=D
        B.subtree_update()
        D.subtree_update()


    def rebalance(A):
        if A.skew() ==2:
            if A.right.skew() < 0:
                A.right.subtree_right_roate()
            A.subtree_left_roate()
        elif A.skew() ==-2:
            if A.left.skew() >0:
                A.left.subtree_left_rotate()
            A.subtree_right_rotate()
    def maintain(A):
        A.rebalance()
        A.subtree_update()
        if A.parent : A.parent.maintain() #lookup the tree (ancestores of current node)



#usage
root=TreeNode(3)
root.insert(6)
root.insert(2)
root.insert(7)
root.insert(5)
root.subtree_iter()
root.rebalance()
root.subtree_iter() # the same  aftre rabalance,because rotation preserve traversal order 

