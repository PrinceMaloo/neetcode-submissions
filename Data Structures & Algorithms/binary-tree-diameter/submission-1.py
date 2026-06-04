# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.maxHeight(root)
        return self.res


    def maxHeight(self, root):
        if(not root):
            return 0
        
        leftHeight = self.maxHeight(root.left)
        rightHeight = self.maxHeight(root.right)
        self.res = max(self.res,leftHeight + rightHeight)
        
        return 1 + max(leftHeight,rightHeight)

        