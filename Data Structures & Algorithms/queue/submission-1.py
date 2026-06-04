class Node:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

class Deque:
    
    def __init__(self):
        self.LinkedList = LinkedList()
                               
    def isEmpty(self) -> bool:
        if(self.LinkedList.head == None):
            return True
        
        return False     

    def append(self, value: int) -> None:
        node = Node(value)
        if(self.LinkedList.head == None and self.LinkedList.tail == None):
            self.LinkedList.head = node
            self.LinkedList.tail = node
            return

        if(self.LinkedList.head.next == None):
            self.LinkedList.tail.next = node
            self.LinkedList.tail = self.LinkedList.tail.next
            self.LinkedList.tail.prev = self.LinkedList.head
            self.LinkedList.head.next = self.LinkedList.tail
            return

        self.LinkedList.tail.next = node
        node.prev = self.LinkedList.tail
        self.LinkedList.tail = self.LinkedList.tail.next
        return

    def appendleft(self, value: int) -> None:
        node = Node(value)

        if(self.LinkedList.head == None and self.LinkedList.tail == None):
            self.LinkedList.head = node
            self.LinkedList.tail = node
            return

        node.next = self.LinkedList.head
        self.LinkedList.head.prev = node
        self.LinkedList.head = node
        return


    def pop(self) -> int:
        if(self.isEmpty()):
            return -1
        ans = -1
        if(self.LinkedList.head == self.LinkedList.tail):
            ans = self.LinkedList.head.val
            self.LinkedList.head = None
            self.LinkedList.tail = None
            return ans
            
        prev = self.LinkedList.tail.prev
        ans = self.LinkedList.tail.val
        prev.next = None
        self.LinkedList.tail = prev
        return ans

    def popleft(self) -> int:
        if(self.isEmpty()):
            return -1
        ans = -1

        if(self.LinkedList.head == self.LinkedList.tail):
            ans = self.LinkedList.head.val
            self.LinkedList.head = None
            self.LinkedList.tail = None
            return ans
        
        ans = self.LinkedList.head.val
        next = self.LinkedList.head.next
        next.prev = None
        self.LinkedList.head = next
        return ans

        

