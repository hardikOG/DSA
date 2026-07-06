class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cardPoints)
        l = 0
        r = n-k
        total = sum(cardPoints[r:])
        res = total
        for r in range(r, n):
            total -= cardPoints[r]
            total += cardPoints[l]
            res = max(total, res)
            l+=1
        return res
        