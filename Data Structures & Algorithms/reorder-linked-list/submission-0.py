# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        reorderListOfValues = []
        curr = head
        while(curr):
            reorderListOfValues.append(curr.val)
            curr = curr.next
        
        orderList = self.orderList(reorderListOfValues)
        curr = head
        i = 0

        while(curr):
            curr.val = orderList[i]
            curr = curr.next
            i += 1
    
    def orderList(self,reorderListOfValues):
        left = 0
        right = len(reorderListOfValues) - 1
        flag = True
        orderList = []

        while(left <= right):
            if(flag):
                orderList.append(reorderListOfValues[left])
                left += 1
            else:
                orderList.append(reorderListOfValues[right])
                right -= 1

            flag = not flag
        
        return orderList





        


        
        