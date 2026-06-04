# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        tailCurr1 = l1
        extra = 0
        length1 = 0
        length2 = 0

        while(curr1):
            length1 += 1
            curr1 = curr1.next

        while(curr2):
            length2 += 1
            curr2 = curr2.next
        
        l3 = l1 if(length1>= length2) else l2
        l4 = l2 if(l1 == l3) else l1
        newHead = l3
        
        while(l3):
            val1 = l3.val
            val2 = l4.val if l4 else 0
            sumValue = val1 + val2 + extra
            nodeValue = sumValue % 10
            extra = (sumValue) // 10
            l3.val = nodeValue

            if(not l3.next):
                tailCurr1 = l3

            l3 = l3.next
            l4 = l4.next if l4 else l4

        if(extra):
            lastNode = ListNode(extra)
            tailCurr1.next = lastNode

        return newHead





        