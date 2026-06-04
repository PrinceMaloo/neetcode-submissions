# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.goodNodesCnt(root,-101)


    def goodNodesCnt(self,root,currMax):
        if not root:
            return 0
        
        ans = 0
        if root.val >= currMax:
            currMax = root.val
            ans += 1
        
        leftCnt = self.goodNodesCnt(root.left,currMax)
        rightCnt = self.goodNodesCnt(root.right,currMax)

        return leftCnt + rightCnt + ans
        