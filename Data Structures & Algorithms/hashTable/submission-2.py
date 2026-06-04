class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    
    def __init__(self, capacity: int):    
        self.map = [None]*capacity
        self.capacity = capacity
        self.size = 0

    def insert(self, key: int, value: int) -> None:
        hash_key = self._getHashKey(key)
        hashnode = self.map[hash_key]

        if hashnode and hashnode.key == key:                                                                                                                                                                        
            self.map[hash_key].value = value
            return
        
        while self.map[hash_key]:
            hash_key = (hash_key + 1) % self.capacity

        self.map[hash_key] = HashNode(key, value)
        self.size += 1

        if self.size >= self.capacity*0.5:
            self.resize()
            hash_key = self._getHashKey(key)


    def get(self, key: int) -> int:
        hash_key = self._getHashKey(key)

        while self.map[hash_key] and self.map[hash_key].key != key:
            hash_key = (hash_key + 1) % self.capacity
        
        if self.map[hash_key] and self.map[hash_key].key == key:
            return self.map[hash_key].value
        
        return -1


    def remove(self, key: int) -> bool:
        hash_key = self._getHashKey(key)
        hashnode = self.map[hash_key]
        temp = (hash_key + 1) % self.capacity

        if hashnode and hashnode.key == key:
            self.map[hash_key] = None
            self.size -= 1
            return True
        
        while self.map[temp] and self.map[temp].key != key and temp != hash_key:
            temp = (temp + 1) % self.capacity
        
        if self.map[temp] and self.map[temp].key == key:
            self.map[temp] = None
            self.size -= 1
            return True
        
        return False

    def getSize(self) -> int:
        return self.size


    def getCapacity(self) -> int:
        print("return", self.capacity)
        return self.capacity

    def resize(self) -> None:  
        new_capacity = 2*self.capacity
        map2 = [None]*new_capacity

        for hashnode in self.map:
            if hashnode:
                hashkey = hashnode.key % new_capacity
                map2[hashkey] = hashnode
            
        self.map = map2
        print("capacity", new_capacity)
        self.capacity = new_capacity


    def _getHashKey(self, key):
        return key % self.capacity

