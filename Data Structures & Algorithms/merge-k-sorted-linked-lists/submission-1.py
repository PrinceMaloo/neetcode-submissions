# Definition for singly-linked list.
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __lt__(self, other):
        return self.val < other.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        min_heap = []
        dummy = ListNode(0)
        head = dummy

        for node in lists:
            if node:
                heapq.heappush(min_heap, [node.val, node])
        
        while min_heap:
            _, node = heapq.heappop(min_heap)
            if node.next:
                heapq.heappush(min_heap, [node.next.val, node.next])
                
            dummy.next = node
            dummy = dummy.next
            
        return head.next
            
                
    