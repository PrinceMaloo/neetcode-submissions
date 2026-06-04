# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        result = []
        while(temp):
            cnt = 0
            subresult = []
            while(cnt < k and temp):
                subresult.append(temp.val)
                temp = temp.next
                cnt += 1
            print('result',result)
            if not temp and cnt < k:
                result += subresult
            else:
                subresult.reverse()
                result += subresult
            
        
        temp = head
        i = 0
        while(temp):
            temp.val = result[i]
            temp = temp.next
            i += 1
        
        return head
            
        