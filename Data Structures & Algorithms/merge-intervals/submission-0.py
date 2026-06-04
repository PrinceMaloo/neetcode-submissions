class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        res.append(intervals[0])

        i = 0
        j = 1
        while(j < len(intervals)):
            if res[i][1] < intervals[j][0]:
                res.append(intervals[j])
                i += 1
            else:
                res[i] = [min(res[i][0], intervals[j][0]), max(res[i][1], intervals[j][1])]
            
            j += 1

        return res
        

