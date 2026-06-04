# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        result = []
        if not root:
            return result

        dq = deque()
        dq.append(root)
        
        while(dq):
            subResult = []
            for i in range(len(dq)):
                curr = dq.popleft()   
                subResult.append(curr.val)              
                if curr.left:
                    dq.append(curr.left)
                if curr.right:
                    dq.append(curr.right)
            
            result.append(subResult)
        
        return result
            
            

            



        