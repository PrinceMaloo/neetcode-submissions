# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        node_set = set([curr.val])
        while curr:
            if curr.val == p.val:
                break
            elif curr.val < p.val:
                curr = curr.right
            else:
                curr = curr.left
            
            node_set.add(curr.val)
        
        curr = root
        result = None
        while curr:
            if curr.val in node_set:
                result = curr
            
            if curr.val == q.val:
                break
            elif curr.val < q.val:
                curr = curr.right
            else:
                curr = curr.left
            
        return result
            


        

            
            
            
            
        