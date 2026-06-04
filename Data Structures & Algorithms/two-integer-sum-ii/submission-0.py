class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers)-1

        while(L<R):
            currentSum = numbers[L]+numbers[R]
            if(currentSum > target):
                R -= 1
            elif(currentSum < target):
                L += 1
            else:
                return [L+1,R+1]


        