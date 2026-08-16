# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        preorder_traversal = []
        self.preorder(root, preorder_traversal)
        
        for i in range(1, len(preorder_traversal)):
            if preorder_traversal[i] <= preorder_traversal[i-1]:
                return False
        
        return True
    

    def preorder(self, root, preorder_traversal):
        if not root:
            return
        
        self.preorder(root.left, preorder_traversal)      
        preorder_traversal.append(root.val)
        self.preorder(root.right, preorder_traversal)
            
        return




        