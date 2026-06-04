class Solution:
    def maxArea(self, heights: List[int]) -> int:

        start = 0
        end = len(heights) -1
        maxAreaResult = -float("inf")

        while(start<end):
            val1 = heights[start]
            val2 = heights[end]
            maxAreaResult = max(maxAreaResult,min(val1,val2)* (end-start))

            if(val1<=val2):
                start += 1
            else:
                end -= 1
        
        return maxAreaResult




        