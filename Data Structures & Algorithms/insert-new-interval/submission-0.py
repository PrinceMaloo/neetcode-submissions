class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start , end = newInterval[0], newInterval[1]

        for interval in intervals:
            if(interval[0] <= start <= interval[1]):
                start = interval[0]
            
            if(interval[0] <= end <= interval[1]):
                end = interval[1]          
        
        result = []

        for interval in intervals:
            if interval[0] < start:
                result.append(interval)
        
            if interval[1] > end:
                result.append(interval)

        result.append([start,end])
        result.sort()
        return result

        