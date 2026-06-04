# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp,next_node, prev_node = head, None, None

        def findkthnode(node, k):
            while(node and k > 1):
                node = node.next
                k -= 1
            
            return node
        
        def reverse(node, k):
            prev = None
            while(node and k):
                temp = node.next
                node.next = prev
                prev = node
                node = temp
                k -= 1
          
            return

        while(temp):
            kth_node = findkthnode(temp, k)

            if not kth_node:
                if temp != head:
                    prev_node.next = temp
                break
            
            next_node = kth_node.next
            reverse(temp, k)

            # print("k",kth_node.val)
            # print("temp",temp.val)
            # if prev_node:
            #     print("pre", prev_node.val)

            if temp == head:
                head = kth_node
            else:
                prev_node.next = kth_node  
            
            
            prev_node = temp
            temp = next_node
        
        return head

