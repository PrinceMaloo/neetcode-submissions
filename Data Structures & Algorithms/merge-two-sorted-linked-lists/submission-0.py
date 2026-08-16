# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1)
        curr = head
        curr1, curr2 = list1, list2

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                temp = ListNode(curr1.val)
                curr.next = temp
                curr1 = curr1.next
            else:
                temp = ListNode(curr2.val)
                curr.next = temp
                curr2 = curr2.next
            
            curr = curr.next

        while curr1:
            temp = ListNode(curr1.val)
            curr.next = temp
            curr1 = curr1.next
            curr = curr.next
        
        while curr2:
            temp = ListNode(curr2.val)
            curr.next = temp
            curr2 = curr2.next
            curr = curr.next
        
        return head.next




        