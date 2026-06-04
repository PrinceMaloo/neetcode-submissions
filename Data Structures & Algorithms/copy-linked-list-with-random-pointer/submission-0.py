"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        newHead = None
        while(curr):
            node = Node(curr.val,curr.next)
            if(curr == head):
                newHead = node
                curr2 = newHead
            else:
                curr2.next = node
                curr2  = curr2.next

            curr = curr.next
        
        curr2 = newHead
        curr = head
        while(curr):
            indexNode = curr.random
            node = curr2
            if(indexNode):
                # print("index",index)
                cnt = 0
                index = 0
                curr3 = newHead
                curr4 = head
                while(curr4):
                    if(curr4 == indexNode):
                        break
                    index += 1
                    curr4 = curr4.next

                print("index",index)
                print("node",node.val)

                while(curr3):
                    if(cnt == index):
                        node.random = curr3
                    curr3 = curr3.next
                    cnt += 1

            curr = curr.next
            curr2  = curr2.next

        return newHead

                



        