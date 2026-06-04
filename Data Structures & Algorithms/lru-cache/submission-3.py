class Node:
    def __init__(self, key, value, prev = None, next = None):
        self.key = key
        self.value = value      
        self.prev = prev
        self.next = next      

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1, self.head)
        self.head.next = self.tail
        self.length = 0

    def get(self, key: int) -> int:
        ptr = self.head

        while(ptr):
            if(ptr.key == key):
                result = ptr.value
                self.change_head_ptr(ptr)
                return result

            ptr = ptr.next
        
        return -1
        
    def put(self, key: int, value: int) -> None:
        ptr = self.head

        while ptr:
            if ptr.key == key:
                ptr.value = value
                self.change_head_ptr(ptr)
                return
            
            ptr = ptr.next
        
        node = Node(key, value)

        if self.length < self.capacity:                      
            self.length += 1         
        else:
            prev_tail = self.tail.prev

            prev_last = prev_tail.prev

            prev_last.next = self.tail

            self.tail.prev = prev_last
  
        self.change_head_ptr(node)  

        return

    
    def change_head_ptr(self, node):
        prev_ptr = node.prev
        next_ptr = node.next

        if prev_ptr:
            prev_ptr.next = next_ptr
        
        if next_ptr:
            next_ptr.prev = prev_ptr
        
        temp = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = temp

        if temp:
            temp.prev = node
    
        
        
            

