class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]
        res = 0

        while l <= r:
            if left_max < right_max:    
                water = max(left_max - height[l] , 0)
                res += water
                left_max = max(left_max, height[l])
                l += 1
            else:
                water = max(right_max - height[r] , 0)
                res += water
                right_max = max(right_max, height[r])
                r -= 1
        
        return res

            