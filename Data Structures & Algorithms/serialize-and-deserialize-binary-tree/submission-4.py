# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
            
        queue = deque([root])
        result = []
        while queue:
            node = queue.popleft()
            if not node:
                result.append(' ')
                continue

            result.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        
        return ','.join(result)


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data: 
            return 
        
        traversal = data.split(',')
        root = TreeNode(int(traversal[0]))
        queue = deque([root])
        index = 1
        while queue:
            node = queue.popleft()
            if index < len(traversal) and traversal[index] != ' ':
                node.left = TreeNode(int(traversal[index]))
                queue.append(node.left)

            index += 1
            if index < len(traversal) and traversal[index] != ' ':
                node.right = TreeNode(int(traversal[index]))
                queue.append(node.right)
            
            index += 1
        
        return root




