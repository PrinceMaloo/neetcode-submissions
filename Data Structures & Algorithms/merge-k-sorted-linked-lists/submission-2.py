# Definition for singly-linked list.
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        min_heap = []
        dummy = ListNode(0)
        head = dummy
        cnt = 0

        for node in lists:
            if node:
                heapq.heappush(min_heap, [node.val,cnt, node])
                cnt += 1
        
        while min_heap:
            _, _, node = heapq.heappop(min_heap)
            if node.next:
                heapq.heappush(min_heap, [node.next.val,cnt, node.next])
                cnt += 1

            dummy.next = node
            dummy = dummy.next
            
        return head.next
            
                
    