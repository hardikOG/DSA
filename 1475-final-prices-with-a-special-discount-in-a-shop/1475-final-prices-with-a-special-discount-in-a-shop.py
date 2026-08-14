class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        res= list(prices)
        st= []
        for i in range(len(prices)):
            while st and prices[i]<=prices[st[-1]]:
                idx= st.pop()
                res[idx] -= prices[i]
            st.append(i)
        return res