

# to return left most child of right sub tree of node to be deleted
def getMinimumKey(curr):
    while curr.left:
        curr = curr.left
    return curr


# Function to delete a node from a BST
def deleteNode(root, key):
    # pointer to store the parent of the current node
    parent = None
    # start with the root node
    curr = root
    # search key in the BST and set its parent pointer
    while curr and curr.data != key:
        # update the parent to the current node
        parent = curr
        # if the given key is less than the current node, go to the left subtree;
        # otherwise, go to the right subtree
        if key < curr.data:
            curr = curr.left
        else:
            curr = curr.right
    
    # return if the key is not found in the tree
    if curr is None:
        return root
    # Case 1: node to be deleted has no children, i.e., it is a leaf node
    if curr.left is None and curr.right is None:
        # if the node to be deleted is not a root node, then set its
        # parent left/right child to None
        if curr != root:
            if parent.left == curr:
                parent.left = None
            else:
                parent.right = None
        # if the tree has only a root node, set it to None
        else:
            root = None
    # Case 2: node to be deleted has two children
    elif curr.left and curr.right:
        # find its inorder successor node  most left  of right sub tree or most right of left 
        successor = getMinimumKey(curr.right)
        # store successor value
        val = successor.data
        # recursively delete the successor. Note that the successor
        # by also continue swaping successor with its inorder successor
        # will have at most one child (right child)
        deleteNode(root, successor.data)
        # copy value of the successor to the current node
        curr.data = val
    # Case 3: node to be deleted has only one child
    else:
        # choose a child node
        if curr.left:
            child = curr.left
        else:
            child = curr.right
        # if the node to be deleted is not a root node, set its parent
        # to its child
        if curr != root:
            if curr == parent.left:
                parent.left = child
            else:
                parent.right = child
        # if the node to be deleted is a root node, then set the root to the child
        else:
            root = child
    return root

    #insertion in BST


    # converting from on traversal order into another
    # from preorder to inorder
'''
    function getInorderFromPreorder(preorder):
    preorderIndex = 0
    inorderIndexMap = createEmptyMap()

    function buildInorder(start, end):
        if start > end:
            return emptyList

        root = preorder[preorderIndex]
        preorderIndex = preorderIndex + 1

        rootIndexInInorder = inorderIndexMap[root]

        leftSubtree = buildInorder(start, rootIndexInInorder - 1)
        rightSubtree = buildInorder(rootIndexInInorder + 1, end)

        return concatenate(leftSubtree, [root], rightSubtree)

    // Initialize the map for quick lookup of indices in the inorder traversal
    for i from 0 to length(inorder) - 1:
        inorderIndexMap[inorder[i]] = i

    // Start the recursive process
    return buildInorder(0, length(preorder) - 1)

// Example usage:
preorder = ['A', 'B', 'D', 'E', 'C', 'F']
inorder = ['D', 'B', 'E', 'A', 'F', 'C']

result = getInorderFromPreorder(preorder)
print(result)
'''
#Function in python
def inorder_from_preorder(preorder):
    def helper(start, end):
        nonlocal index
        if start > end:
            return []
        
        root = preorder[index]
        index += 1

        root_index_in_inorder = inorder_index[root] #map for inorder element indices 

        left_subtree = helper(start, root_index_in_inorder - 1)
        right_subtree = helper(root_index_in_inorder + 1, end)

        return left_subtree + [root] + right_subtree # just concat lists together
    
    index = 0
    inorder_index = {value: i for i, value in enumerate(inorder)}

    return helper(0, len(preorder) - 1)

# Example usage:
preorder = ['A', 'B', 'D', 'E', 'C', 'F']
inorder = ['D', 'B', 'E', 'A', 'F', 'C']

result = inorder_from_preorder(preorder)
print(result)



#quick sort in python 
