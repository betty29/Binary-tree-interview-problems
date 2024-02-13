'''
Check if two binary trees are identical or not – Iterative and Recursive
Write an efficient algorithm to check if two binary trees are identical or not. Two binary trees are identical if they have identical structure and their contents are also the same.
Leetcode link - 
Problem 

Input 

Tree 1
                1
               / \
              2   3
             / \  /\
            4   5 6 7

Tree 2
                1
               / \
              2   3
             / \  /\
            4   5 6 7

Output : True
Both binary trees have the same structure and contents.
'''

class Node:
    def __init__(self,value= None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
        
def sameTreesOrNot(root1, root2):
    # are both the trees having the sames structure?
    # 3 base cases 
    # if both have reached the end then return true (checking values in return condition itself)
    if(not root1 and not root2):
        return True
        
    # one of the tree's node is null
    if(not root1 or not root2):
        return False
    if(root1.value != root2.value):
        return False
        
    return sameTreesOrNot(root1.left, root2.left) and sameTreesOrNot(root1.right, root2.right)
    
    
if __name__ == "__main__":
    
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)
    root1.right.left = Node(6)
    root1.right.right = Node(7)
    
    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(3)
    root2.left.left = Node(4)
    root2.left.right = Node(5)
    root2.right.left = Node(6)
    root2.right.right = Node(7)
    
    
    print(sameTreesOrNot(root1, root2))