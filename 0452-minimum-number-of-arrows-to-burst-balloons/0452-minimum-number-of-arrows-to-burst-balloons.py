class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        points.sort()
        arrows = 1
        prevEnd = points[0][1]
        for start, end in points[1:]:
            if start>prevEnd:
                arrows+=1
                prevEnd = end
            else:
                prevEnd = min(prevEnd, end)
        return arrows