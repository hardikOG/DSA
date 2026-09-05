class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        intervals.sort()
        res = [intervals[0]]
        for start, end in intervals[1:]:
            prevEnd = res[-1][1]
            if start<= prevEnd:
                res[-1][1] = max(prevEnd, end)
            else:
                res.append([start, end])
        return res

