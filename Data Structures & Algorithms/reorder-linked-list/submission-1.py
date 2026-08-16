# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow_ptr, fast_ptr = head, head
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        
        curr1, curr2, slow_ptr.next = head, slow_ptr.next, None
        curr2 = self.reverseList(curr2)

        while curr2:
             tmp1, tmp2 = curr1.next, curr2.next
             curr1.next = curr2
             curr2.next = tmp1
             curr1, curr2 = tmp1, tmp2
        return

    def reverseList(self, head):
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev


        