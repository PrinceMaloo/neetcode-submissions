# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return 
        
        if len(lists) == 1:
            return lists[0]
        
        first, second = lists[0], self.mergeKLists(lists[1:])
        result = self.mergeTwoSortedLists(first, second)
        return result
    
    def mergeTwoSortedLists(self, first: ListNode, second: ListNode) -> ListNode:
        dummy = ListNode(0)
        head = dummy

        while first and second:
            if first.val <= second.val:
                dummy.next = first
                first = first.next
            else:
                dummy.next = second
                second = second.next
            
            dummy = dummy.next
        
        if first:
            dummy.next = first

        if second:
            dummy.next = second
        
        return head.next
         


        