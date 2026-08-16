# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([(root, 1)])
        result = 0
        while queue:
            node, cnt = queue.popleft()
            result = max(result, cnt)
            if node.left:
                queue.append((node.left, cnt + 1))
            
            if node.right:
                queue.append((node.right, cnt + 1))
        
        return result
            
            
        