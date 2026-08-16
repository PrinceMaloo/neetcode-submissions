class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        for i in range(len(heights)):
            sub_result = 0
            l, r = i, len(heights) - 1
            while l < r:
                sub_result = max(sub_result, (r-l)*min(heights[l], heights[r]))
                r -= 1
            
            result = max(result, sub_result)
        
        return result

        