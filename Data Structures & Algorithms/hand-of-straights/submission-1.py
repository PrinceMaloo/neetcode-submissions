class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        
        groups = int(n / groupSize)
        map = {}

        for num in hand:
            map[num] = map.get(num, 0) + 1
        
        hand.sort()

        for val in hand:
            if map[val] == 0:
                continue
            
            for j in range(val, val + groupSize):
                if j not in map or map[j] == 0:
                    return False

                map[j] -= 1

        return True