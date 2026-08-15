# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return (0, 0)
            
            left_rob, left_not = dfs(root.left)
            right_rob, right_not = dfs(root.right)
            left_rob, right_rob = (
                max(left_rob, left_not), 
                max(right_rob, right_not)
            )

            return (root.val + left_not + right_not, left_rob + right_rob)
        
        return max(dfs(root))
        