class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []

        n = len(digits) - 1
        resulting_sum = 0
        for digit in digits:
            resulting_sum += (digit)*(10**n)
            n -= 1
        
        resulting_sum += 1

        while(resulting_sum):
            result.append(resulting_sum % 10)
            resulting_sum = resulting_sum // 10
        
        result.reverse()
        return result

        