class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = {}
        for index, ch in enumerate(s):
            if ch not in hashmap:
                hashmap[ch] = [index, index]
            else:
                hashmap[ch][1] = index
        
        noi = []
        for interval in hashmap.values():
            if len(noi) == 0:
                noi.append(interval)
            elif interval[0] < noi[-1][1]:
                noi[-1][1] = max(noi[-1][1], interval[1])
            else:
                noi.append(interval)
        
        return [(end- start + 1) for (start, end) in noi]