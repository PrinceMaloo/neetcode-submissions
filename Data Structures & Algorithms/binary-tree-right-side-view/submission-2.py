# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        d = deque()
        res = []
        if root:
            d.append(root)
    
        while(d):
            list = []
            for i in range(len(d)):
                curr = d.popleft()
                list.append(curr.val)               
                if curr.left:
                    d.append(curr.left)
                if curr.right:
                    d.append(curr.right)
                
            res.append(list[-1])
        
        return res
            
                




        