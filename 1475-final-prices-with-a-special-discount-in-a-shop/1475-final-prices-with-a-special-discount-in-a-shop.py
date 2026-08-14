class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        stack = []
        res = prices[:]
        for i,p in enumerate(prices):
            while stack and prices[stack[-1]]>=p:
                val = stack.pop()
                res[val] = prices[val] - p
            stack.append(i)
        return res