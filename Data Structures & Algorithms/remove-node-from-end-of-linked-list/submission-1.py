# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        position = length - n + 1
        prev, curr = None, head
        for i in range(1, position):
            prev = curr
            curr = curr.next

        if position == 1:
            return head.next

        prev.next, curr.next = curr.next, None
        return head

        


            


