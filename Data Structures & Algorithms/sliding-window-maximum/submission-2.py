import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        heap = []
        for index, num in enumerate(nums):
            heapq.heappush(heap, (-num, index))

            if index >= k-1:
                while heap[0][1] <= index - k:
                    heapq.heappop(heap)

                result.append(-heap[0][0])
            
        return result



            


        