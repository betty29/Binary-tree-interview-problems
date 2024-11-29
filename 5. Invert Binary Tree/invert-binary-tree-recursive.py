# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# respective to the node, the right child and the left child are swapped
# recursion
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # base condition 

        if not root:
            return None
        
        # swapping the children
        tmp = root.left
        root.left = root.right
        root.right= tmp

#       recursively swap the children of left subtree and the right subtree 
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root