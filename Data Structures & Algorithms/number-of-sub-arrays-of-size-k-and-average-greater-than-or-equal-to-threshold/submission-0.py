class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        L = 0
        n = len(arr)
        cnt = 0
        windowSum = 0


        for R in range(n):
            if(R-L >= k):         
                windowSum -= arr[L]
                L += 1
            windowSum += arr[R]
           
            if((windowSum)/k >= threshold and R>=k-1):
                cnt += 1

        return cnt


            



        