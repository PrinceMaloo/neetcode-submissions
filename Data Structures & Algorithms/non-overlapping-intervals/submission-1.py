class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[0])
        
        def dfs(index, prev):
            if index == len(intervals):
                return 0
            
            res = dfs(index + 1, prev)
            if prev == -1 or intervals[prev][1] <= intervals[index][0]:
                res = max(res, 1 + dfs(index + 1, index))
            
            return res
        
        return len(intervals) - dfs(0, - 1)



        