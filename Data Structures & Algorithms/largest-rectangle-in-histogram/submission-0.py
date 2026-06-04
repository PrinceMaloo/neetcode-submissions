class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        result = 0
        for i in range(n):
            j = i 
            min_height = float("inf")
            sublevel_max_area = 0
            while(j < n and heights[j] != 0):
                width = j - i + 1
                min_height = min(heights[j], min_height)
                sublevel_max_area = max(sublevel_max_area, width * min_height)
                j += 1
            
            result = max(result,sublevel_max_area)
        
        return result