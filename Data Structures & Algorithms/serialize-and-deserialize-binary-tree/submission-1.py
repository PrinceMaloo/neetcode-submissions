# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Traversal: 
    @staticmethod
    def preorder_traversal(root, array):
        if not root:
            return
        
        array.append(root.val)
        Traversal.preorder_traversal(root.left, array)
        Traversal.preorder_traversal(root.right, array)
        return

    @staticmethod
    def inorder_traversal(root, array):
        if not root:
            return
        
        Traversal.inorder_traversal(root.left, array)
        array.append(root.val)
        Traversal.inorder_traversal(root.right, array)
    
    @staticmethod
    def create_tree(preorder, inorder):
        if not preorder:
            return
        
        root_val = preorder[0]

        root = TreeNode(root_val)

        reverse_inorder = inorder[::-1]

        root_inorder_index = len(inorder) - 1 - reverse_inorder.index(root_val)

        root.left = Traversal.create_tree(preorder[1:root_inorder_index + 1], inorder[:root_inorder_index])
        
        root.right = Traversal.create_tree(preorder[root_inorder_index + 1:], inorder[root_inorder_index + 1:])

        return root

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        preorder = []
        inorder = []

        Traversal.preorder_traversal(root, preorder)
        Traversal.inorder_traversal(root, inorder)

        preorder_string = "*".join([str(i) for i in preorder])
        inorder_string = "&".join([str(i) for i in inorder])

        print("preorder_string",preorder_string)
        print("inorder_string", inorder_string)

        result = preorder_string + '|' + inorder_string
        return result
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        preorder = data.split('|')[0].split('*')
        inorder = data.split('|')[1].split('&')

        print("preorder",preorder , len(preorder))
        print("preorder",inorder , len(inorder))

        if  preorder[0] == '':
            return 

        preorder = [int(i) for i in preorder]
        inorder = [int(i) for i in inorder]

        root = Traversal.create_tree(preorder, inorder)
        return root
        


