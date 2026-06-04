class Solution:
    def jump(self, nums: List[int]) -> int:
        
        def bfs(index):
            if index == len(nums)-1:
                return 0

            queue = deque()
            visit = set()
            queue.append((index, 0))
            visit.add(0)
            result = 0

            while(queue):
                position, step = queue.popleft()
                for i in range(1, nums[position] + 1):
                    next_step = step + 1
                    next_position = position + i
                    if next_position >= len(nums) - 1:
                        result = next_step
                        return result
                    if next_position not in visit: 
                        queue.append((next_position, next_step))
                        visit.add(next_position)

            return result
        
        return bfs(0)
                