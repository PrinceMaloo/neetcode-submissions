# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        prev = None
        curr1 = curr2 = head
        position = 0
        cnt = 0
        while(curr1):
            length += 1
            curr1 = curr1.next
        
        position = length  - n + 1

        if(position == 1):
            head = head.next
            return head


        while(curr2):
            cnt += 1
            if(cnt == position):
                prev.next = curr2.next
                curr2.next = None
                return head

            prev = curr2
            curr2 = curr2.next





        