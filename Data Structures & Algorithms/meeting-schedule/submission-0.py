"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        ab = sorted(intervals, key = lambda a: a.start)
        
        prevEndTime = 0
        for i in range(len(ab)):
            if prevEndTime > ab[i].start:
                return False
            prevEndTime = ab[i].end

        return True
