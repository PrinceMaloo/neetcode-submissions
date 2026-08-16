# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:        
        queue1, queue2 = deque([p]), deque([q])

        while queue1 and queue2:
            node1, node2 = queue1.popleft(), queue2.popleft()

            if not node1 and not node2:
                continue

            if (not node1 and node2) or (not node2 and node1) or node1.val != node2.val:
                return False
            
            if node1:
                queue1.append(node1.left)
                queue1.append(node1.right)
            
            if node2:
                queue2.append(node2.left)
                queue2.append(node2.right)
            
        
        return len(queue1) == len(queue2)


        

        