from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        if key not in self.map:
            return result
        
        values = self.map[key]
        
        l = 0
        r = len(values) - 1

        while(l <= r):
            m = (l + r)//2
            if(values[m][0] == timestamp):
                result = values[m][1]
                break
            elif(values[m][0] < timestamp):
                result = values[m][1]
                l = m + 1
            else:
                r = m - 1
        
        return result




        
