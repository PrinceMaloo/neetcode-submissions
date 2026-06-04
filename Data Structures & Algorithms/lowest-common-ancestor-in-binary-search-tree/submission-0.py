# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        preorderResult = self.preorder(root)
        inorderResult = self.inorder(root)

        print("preorderResult",preorderResult)
        print("postorderResult",inorderResult)
        rootIndexInOrder = 0
        for i in range(len(inorderResult)):
            if(inorderResult[i] == root.val):
                rootIndexInOrder = i
                break

        leftHalfOfRoot = inorderResult[0:rootIndexInOrder]
        rightHalfOfRoot = inorderResult[rootIndexInOrder+1:]
        bothValuesAreInOppositeSide = False

        print("leftHalfOfRoot",leftHalfOfRoot)
        print("rightHalfOfRoot",rightHalfOfRoot)

        if((p.val in leftHalfOfRoot and q.val in rightHalfOfRoot) 
            or (q.val in leftHalfOfRoot and p.val in rightHalfOfRoot)):
            bothValuesAreInOppositeSide = True

        
        if(p.val == root.val or q.val == root.val or bothValuesAreInOppositeSide):
            return root

        if(p.val in leftHalfOfRoot):
            return self.lowestCommonAncestor(root.left,p, q )
        else:
            return self.lowestCommonAncestor(root.right,p, q )

    def preorder(self,root,array= None):
        if array is None:
            array = []
        if not root:
            return array
        array.append(root.val)
        self.preorder(root.left,array)
        self.preorder(root.right,array)
        return array
    
    def inorder(self,root,array= None):
        if array is None:
            array = []
        if not root:
            return array 

        self.inorder(root.left,array)
        array.append(root.val)
        self.inorder(root.right,array)
        
        return array

        
        
        