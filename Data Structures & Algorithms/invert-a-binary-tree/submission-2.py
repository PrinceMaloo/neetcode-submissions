# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        queue = deque([root])
        node_list = []
        while queue:
            node = queue.popleft()
            node_list.append(node)
            if node:
                queue.append(node.right)
                queue.append(node.left)
        
        head = node_list[0]
        print("node", node_list)
        i, j = 0, 1
        while i < j < len(node_list):
            root = node_list[i]
            if root:
                root.left = node_list[j]
                root.right = node_list[j + 1]
                j += 2

            i += 1
        
        return head

        
            
            


        

        