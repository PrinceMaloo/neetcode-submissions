# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        result = True

        if root.left:
            left_max = self.dfs(root.left, False)
            result = result and (left_max < root.val)
        
        if root.right:
            right_min = self.dfs(root.right, True)
            result = result and (right_min > root.val)
        
        if not result:
            return result

        result = result and self.isValidBST(root.left) and self.isValidBST(root.right)

        return result
    
    def dfs(self, root, min_value):
        queue = deque()
        queue.append(root)
        result = root.val

        while queue:
            node = queue.popleft()

            if min_value:
                result = min(node.val, result)
            else:
                result = max(node.val, result)

            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
        
        return result




        
            




