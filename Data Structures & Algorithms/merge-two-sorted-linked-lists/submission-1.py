# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
       
       node = ListNode()
       if(list1 and list2 and list1.val <= list2.val):
        resultantHead = list1
       elif(list1 and list2 and list1.val > list2.val):
        resultantHead = list2
       else:
        resultantHead = list1 or list2
    
    

    


       
       while(list1 and list2):

        val1 = list1.val
        val2 = list2.val

        if(val1 <= val2):
            node.next = list1
            list1 = list1.next  
        else:
            node.next = list2
            list2 = list2.next
            
        node = node.next
       
       node.next = list1 or list2
        
       return resultantHead
        
        
        

            
            

