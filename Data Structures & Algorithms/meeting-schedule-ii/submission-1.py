"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        cnt = 0
        rooms = {}

        intervals.sort(key = lambda x : x.start)

        for interval in intervals:
            start, end = interval.start, interval.end
            new_room = True
            for (i, (_,e)) in rooms.items():
                if start >= e:
                    rooms[i] = (start,end)
                    new_room = False
                    break
            
            if new_room:
                cnt += 1
                rooms[cnt] = (start,end)
        
        return len(rooms)
                
                


        