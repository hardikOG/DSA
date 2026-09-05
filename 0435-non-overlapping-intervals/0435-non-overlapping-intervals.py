class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) <= 1:  #edge case
            return 0
        intervals.sort()
        removed = 0
        prevEnd = intervals[0][1]    #for keeping track of the previous interval
        for start, end in intervals[1:]:
            if start<prevEnd:
                removed+=1  #current interval starts before prevEnd, there is an overlap
                prevEnd = min(prevEnd, end)  #keep the interval with the smaller ending time
            else:
                prevEnd = end  #update it to current interval's end
        return removed