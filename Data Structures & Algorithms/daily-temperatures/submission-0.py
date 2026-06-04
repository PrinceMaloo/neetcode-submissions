class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = []

        for i in range(len(temperatures)):
            subResult = 0
            for j in range(i+1,len(temperatures)):
                if(temperatures[j] > temperatures[i]):
                    subResult = j - i
                    break
            result.append(subResult)

        return result


        

        