from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        queue = deque()
        
        max_heap = [-v for v in count.values()]
        heapq.heapify(max_heap)

        time = 0

        while max_heap or queue:     
            time += 1
            
            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt: 
                    queue.append((cnt,time + n))
        
            if queue and queue[0][1] == time:
                cnt, _ = queue.popleft()
                heapq.heappush(max_heap, cnt)
                
        return time



        