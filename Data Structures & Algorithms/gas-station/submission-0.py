class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        for i in range(n):
            available_gas, solution_exist = 0, True
            for index in range(i, n + i):
                if(available_gas < 0):
                    solution_exist = False
                    break
                
                available_gas += gas[index % n] - cost[index % n]

            if(solution_exist and available_gas >= 0):
                return i
            
        return -1
        