# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if(root is None and subRoot is not None):
            return False
            
        if(root is None and subRoot is None):
            return True

        flag = self.isSameTree(root,subRoot)

        if(flag):
            return flag

        return flag or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
    
    def isSameTree(self,root,subRoot):
        q1 = deque()
        q2 = deque()

        q1.append(root)
        q2.append(subRoot)

        while(q1 and q2):
            for _ in range(len(q1)):
                e1 = q1.popleft()
                e2 = q2.popleft()
                
                if(e1 is None and e2 is None):
                    continue
                
                if(e1 is None or e2 is None or e1.val != e2.val):
                    return False
                
                q1.append(e1.left)
                q1.append(e1.right)
                q2.append(e2.left)
                q2.append(e2.right)
            
        return True

        

        
    