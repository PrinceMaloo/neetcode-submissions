# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.dfs(root,0,res)
        return res
    

    def dfs(self,root,depth,res):
        if not root:
            return None
        
        if depth == len(res):
            res.append(root.val)
        
        self.dfs(root.right,depth + 1,res)
        self.dfs(root.left,depth + 1,res)
        
        
        