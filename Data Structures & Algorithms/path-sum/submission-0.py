# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        subSum = 0
        return self.hasPathSums(root,targetSum,subSum)
    
    def hasPathSums(self,root,targetSum,subSum):
        subSum += root.val
        if(root.left == None and root.right == None):
            if(subSum == targetSum):
                return True

        Result1 = False
        Result2 = False    
        if root.left:
            Result1 = self.hasPathSums(root.left,targetSum,subSum)

        if root.right:
            Result2 = self.hasPathSums(root.right,targetSum,subSum)
        
        return (Result1 or Result2)

        
        