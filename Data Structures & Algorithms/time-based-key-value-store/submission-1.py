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
        recent_index = -1
        for index,(time,val) in enumerate(values):
            if time == timestamp:
                result = val
                break
            elif time < timestamp:
                recent_index = index
            else:
                continue

        if(not result and recent_index != -1):
            result = values[recent_index][1]
        
        return result




        
