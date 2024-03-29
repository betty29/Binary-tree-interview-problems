'''
In preorder traversal, the root is processed/visited first and then the left subtree and the right subtree

Leetcode link - https://leetcode.com/problems/binary-tree-preorder-traversal/description/
Problem 144
'''

class Node:
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
        
def preorder(root):
    
    # current node is empty
    if root is None:
        return 
    
     # print the value  or process the node
    print(root.value, end = ' ') 
    
    # recursively call left subtree for each node
    preorder(root.left)
    
    # recursively call right subtree for each node
    preorder(root.right)
    

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
    
    preorder(root)

    