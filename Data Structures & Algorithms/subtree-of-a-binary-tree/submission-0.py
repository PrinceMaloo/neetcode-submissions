# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
            
        if self.isSameTree(root, subRoot):
            return True
        
        result = False
        if root.left:
            result = result or self.isSubtree(root.left, subRoot)
        
        if root.right:
            result = result or self.isSubtree(root.right, subRoot)
        
        return result
        

    
    def isSameTree(self, root1, root2):
        if not root1 and not root2:
            return True
        
        if not root1 or not root2 or root1.val != root2.val:
            return False
        
        return self.isSameTree(root1.left, root2.left) and self.isSameTree(root1.right, root2.right)
        