'''
In postorder traversal, the left subtree and the right subtree is visited first and then  the root is processed/visited 

Leetcode link - https://leetcode.com/problems/binary-tree-postorder-traversal/description/
Problem 145
'''

class Node:
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
        
def postorder(root):
    
    # current node is empty
    if root is None:
        return 
    
   
    
    # recursively call left subtree for each node
    postorder(root.left)
    
    # recursively call right subtree for each node
    postorder(root.right)

    # print the value  or process the node
    print(root.value, end = ' ') 
    

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
    
    postorder(root)

    