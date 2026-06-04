# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        last = secondLast = None
        while(curr):
            if(not curr.next):
                last = curr
            
            if(curr.next and (not curr.next.next)):
                secondLast = curr
            
            curr = curr.next
        
        if(not (last and secondLast)):
            return 

        if(secondLast == head):
            return 

        secondLast.next = None
        last.next = head.next
        head.next = last

        self.reorderList(head.next.next)


        
        


      