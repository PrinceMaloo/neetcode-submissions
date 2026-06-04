class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        
        groups = int(n / groupSize)
        map = {}

        for num in hand:
            map[num] = map.get(num, 0) + 1

        for i in range(groups):
            starting_value = self.find_groupkey(map)

            for j in range(starting_value, starting_value + groupSize):
                if j not in map or map[j] == 0:
                    return False
                
                map[j] -= 1
        
        return True
        
    def find_groupkey(self, map):
        result = float("inf")
        for key, val in map.items():
            if val > 0:
                result = min(result, key)
            
        return result


        