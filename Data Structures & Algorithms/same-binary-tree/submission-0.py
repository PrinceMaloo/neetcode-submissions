# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque()
        q2 = deque()

        q1.append(p)
        q2.append(q)

        if(len(q1) != len(q2)):
            return False

        while(q1 and q2):
            if(len(q1) != len(q2)):
                return False

            e1 = q1.popleft()
            e2 = q2.popleft()

            if(e1 is None and e2 is not None):
                return False

            if(e1 is not None and e2 is None):
                return False

            if(e1 is not None and e2 is not None and e1.val != e2.val ):
                return False

            if(e1 is not None):
                q1.append(e1.left)
                q1.append(e1.right)

            if(e2 is not None):
                q2.append(e2.left)
                q2.append(e2.right)

        return True

            
            









        