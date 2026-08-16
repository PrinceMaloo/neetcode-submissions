# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        preorder_traversal = []
        self.preorder(root, preorder_traversal)
        
        return preorder_traversal[k-1]
        
    

    def preorder(self, root, preorder_traversal):
        if not root:
            return
        
        self.preorder(root.left, preorder_traversal)      
        preorder_traversal.append(root.val)
        self.preorder(root.right, preorder_traversal)
            
        return