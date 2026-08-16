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
        
        curr1, curr2 = head, slow_ptr.next
        slow_ptr.next = None
        curr2 = self.reverseList(curr2)

        flag = True
        while curr1 and curr2:
            if flag:
                temp = curr1.next
                curr1.next = curr2
                curr1 = temp
                flag = False
            else:
                temp = curr2.next
                curr2.next = curr1
                curr2 = temp
                flag = True
        
        return

    def reverseList(self, head):
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev


        