# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    
        subSum = 0
        return self.hasPathSums(root,targetSum,subSum)
    
    def hasPathSums(self,root,targetSum,subSum):
        if not root:
            return False
            
        subSum += root.val
        if(root.left == None and root.right == None):
            if(subSum == targetSum):
                return True

        return (self.hasPathSums(root.left,targetSum,subSum) or self.hasPathSums(root.right,targetSum,subSum))

        
        