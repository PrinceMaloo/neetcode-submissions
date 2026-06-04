class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if(sum(gas) < sum(cost)):
            return -1
        n = len(gas)
        final_available_gas = 0
        result = float("inf")
        for i in range(n):
            diff = gas[i] - cost[i]
            final_available_gas += diff
            if(final_available_gas < 0):
                final_available_gas = 0
                result = float("inf")
            else:
                result = min(result,i)
                  
        return result



        