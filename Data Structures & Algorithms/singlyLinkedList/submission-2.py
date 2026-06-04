class LinkedNode:
    def __init__(self,value = -1):
        self.val = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None

    
    def get(self, index: int) -> int:

        temp = self.head
        i = 0
        
        while(temp != None):
            if(i == index):
                return temp.val
            
            temp = temp.next
            i += 1
        
        return -1

    def insertHead(self, val: int) -> None:
        Node = LinkedNode(val)
        if(self.head == None):
            self.tail = Node

        Node.next = self.head
        self.head = Node

    def insertTail(self, val: int) -> None:
        Node = LinkedNode(val)
        if(self.tail == None):
            self.head = Node
            self.tail = Node
            return

        self.tail.next = Node
        self.tail = Node
        

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        prev = self.head

        

        while(curr != None and i <= index): 
            if(i == index):
                if(curr.next == None):
                    self.tail = prev

                if(index == 0):
                    if(self.head == self.tail):
                        self.tail = None
                        self.head = None
                        return True

                    self.head = self.head.next 
                    return True

                prev.next = curr.next
                curr.next = None
                return True

            i += 1
            prev = curr
            curr = curr.next

        return False

    def getValues(self) -> List[int]:

        result = []
        temp = self.head

        while(temp != None):
            result.append(temp.val)
            temp = temp.next

        return result

















        
