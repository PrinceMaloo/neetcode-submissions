class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        result = []
        for num in nums:
            if len(queue) == k:
                max_num = max(queue)
                result.append(max_num)
                queue.popleft()
            
            queue.append(num)
        
        if queue:
            max_num = max(queue)
            result.append(max_num)
        
        return result


            


        