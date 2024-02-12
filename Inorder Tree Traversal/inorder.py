'''
This is a recursive approach for the inorder traversal of a binary tree.

The recursive approach is a depth first search implementation (graph algorithm) as the search tree is deepened on 
each child before moving on to the next siblings.
'''


class Node:
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
        
def inorder(root):
    
    # current node is empty
    if root is None:
        return 
    
    # recursively call left subtree for each node
    inorder(root.left)
    
    # print the value  or process the node
    print(root.value, end = ' ')
    
    # recursively call right subtree for each node
    inorder(root.right)
    

if __name__ == "__main__":
    
    '''
    consider the tree
    
               5
             /   \
            /     \
           6       7
          /      /   \
         /      /     \
        8      9       10
              / \
             /   \
            11   12
    '''
    root = Node(5)
    root.left = Node(6)
    root.left.left = Node(8)
    root.right = Node(7)
    root.right.left = Node(9)
    root.right.right = Node(10)
    root.right.left.left = Node(11)
    root.right.left.right = Node(12)
    
    inorder(root)
