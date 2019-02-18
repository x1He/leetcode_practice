# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        intervals.sort(key = lambda x: x.start)

        res = []

        for item in intervals:
            if not res or res[-1].end < item.start:
                res.append(item)

            else:
                res[-1].end = max(res[-1].end, item.end)

        return res
