# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = [root.val]
        def dfs(root):
            if not root:
                return 0

            res  = root.val    
            left_res = max(dfs(root.left), 0)
            right_res = max(dfs(root.right), 0)
            res = max(left_res,right_res)+ root.val                 
            result[0] = max(result[0], root.val + left_res + right_res)
            return res
        
        dfs(root)
        return result[0]
