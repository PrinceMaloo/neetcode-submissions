class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxAreaResult = -float("inf")
        for (i,value) in enumerate(heights):
            for j in range(i+1,len(heights)):
                value2 = heights[j]
                maxAreaResult = max(maxAreaResult, min(value,value2)*(j-i))
        
        return maxAreaResult


        