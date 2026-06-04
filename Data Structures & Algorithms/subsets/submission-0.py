class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        output = [[]]

        for num in nums:
            loopRange = len(output)
            for i in range(loopRange):
                out = output[i].copy()
                out.append(num) 
                output.append(out)

        return output


        