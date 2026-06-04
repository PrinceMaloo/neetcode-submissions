class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        result = [-1]*len(queries)
        intervals.sort(key = lambda x : x[0])
        for index, query in enumerate(queries):
            for interval in intervals:
                if query < interval[0]:
                    break
                    
                if interval[0] <= query <= interval[1]:
                    result[index] = min(result[index], interval[1] - interval[0] + 1) if result[index] != -1 else interval[1] - interval[0] + 1          
                
        return result