#traversal operaions 

#definition of the node 
class TreeNode:
  def __init__(self, value):
    self.value = value # data
    self.right = None # references to right child d
    self.left  = None # reference to left child 
  def insert(self, data):
    # Compare the new value with the parent node
      if self.value:
         if data < self.value:
            if self.left is None:
               self.left = TreeNode(data)
            else:
               self.left.insert(data)
         elif data > self.value:
               if self.right is None:
                  self.right = TreeNode(data)
               else:
                  self.right.insert(data)
      else:
         self.value = data

  # inorder traversal 
  def printTree(self):
      if self.left:
        self.left.printTree()

      print( self.value)

      if self.right:
         self.right.printTree()
     


def node_parent(node,node1):
   if not node:
       return None
   if node.left==node1 or node.right==node1:
       return node
   return node_parent(node.left,node1) or node_parent(node.right,node1)


# subtree_first(node)
" - find first node in the traversal order of node <X>’s subtree (last is symmetric) "
" - If <X> has left child, recursively return the first node in the left subtree "
" - Otherwise, <X> is the first node, so return it "
" - Running time is O(h) where h is the height of the tree the best running time with BST where height is lg(n)"


def subtree_first(node):
    if not node or not node.left:
        return node
    if not node.left and not node.right:
          return node
    return subtree_first(node.left)
########## 
def subtree_last(node):
    if not node or not node.right :
        return node
    if not node.right and not node.left:
        return node
    return subtree_last(node.right)   


{ # algorithm
" - Find successor of node <X> in the traversal order (predecessor is symmetric) "
" - If <X> has right child, return first of right subtree "
" - Otherwise, return lowest ancestor of <X> for which <X> is in its left subtree "
" - Running time is O(h) where h is the height of the tree "
}


#successor(node)

def successor(root, node):
   if not node:
      return None
   
   #first case when node has right child then return subtree first node of right subtree
   if node.right:
      return subtree_first(node.right)
   # case 2 when node doesn't have right child then reuturn LCA (lowest common ancestor of this node with its parent)
   return find_ancestor(root, node)
########### 
def find_successor(root, target):
    if not root or not target:
        return None
    # Case 1: If the target node has a right subtree,
    # return the leftmost node in that subtree
    if target.right:
        return subtree_first(target.right)

    # Case 2: If the target node does not have a right subtree,
    # find the lowest ancestor for which target is in its left subtree
    return find_ancestor(root, target)

def predeccessor(root , node):
    if not node:
        return None  
    if node.left:
        return subtree_last(node.left)
    return find_ancestor(root,node)

def find_ancestor(root, target):
    if not root:
        return None

    if root == target or (ancestor := find_ancestor(root.left, target)) or (ancestor := find_ancestor(root.right, target)):
        return root
    
    return ancestor

def insert_after(node , new):
    # insert after when mean in treversal order ( inorder traversal) and after is the direst left child or its subtree_first
    if not node.right:
        node.right=new
    # case 2 when node has a right child 
    # then when insert new node as left child of left most node of right subtree
    else:
        subtree_first_node=subtree_first(node.right)
        subtree_first_node.left=new 
    # we have guarantee that subtree_first_node node is the node with no left child
# Lowst Common Ancestor of Binary Tree
def lowestCommonAncestor(self, root, p, q):
    def dfs(curr,p,q):
        #base case 1
        if not curr:
            return None
        #coverage case 
        #current node equal one of two target nodes 
        if curr==q or curr==p:
            return curr
        #search left and right subtree
        left=dfs(curr.left,p,q)
        right=dfs(curr.right,p,q)
        # if both are not null
        # exists in both subtrees
        # then root is LCA
        if left and right:
            return curr
        # case when they exist is the same subtree 
        # then return the KCA either left or right
        return left or right
        # call for recursive function 
    return dfs(root,p,q)
        
# first we will search for this node if we find it then 
#if it's leaf then return None if
# it's not then find it's predeccessor and swap them 
# i wanna first find this node and its parent in the tree 
#def subtree_delete(root, node): 

def find_parent(root, key, parent=None):
    if root is None:
        return None

    if root.value == key:
        return parent

    # Recur on the left and right subtrees
    left_parent = find_parent(root.left, key, root)
    right_parent = find_parent(root.right, key, root)

    # Return the node and its parent if found in either subtree
    if left_parent:
        return left_parent
    elif right_parent:
        return right_parent
    else:
        return None


#Example of usage 

root = TreeNode(15)
root.insert(2)
root.insert(4)
root.insert(17)
root.insert(9)
root.insert(20)
root.insert(16)
# Find the successor of a node (e.g., node with value 2)

#target_node = root.left.right
#successor_node = find_successor(root, target_node)
#subtree_first_node= subtree_first(root.left)
# root=subtree_delete(root,root.left.right)


#if successor_node:
   # print(f"The successor of {target_node.value} is {successor_node.value}")
#else:
   # print(f"{target_node.value} does not have a successor.")

# subtree_first_node of the left subtree 
#if subtree_first_node:
    # print(f"the left most node of the left subtree is : {subtree_first_node.value}")
#print("tree after deletion of node 5 is ")
root.printTree()


# iam stull stuck with delete node but the implementation of code in lecture notes solve this with the implementation of 
# predeccessor and successor and parent field in node but i'll continue on this 