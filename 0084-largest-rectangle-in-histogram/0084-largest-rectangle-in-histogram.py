class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        st = []
        best = 0
        for i,h in enumerate(heights+ [0]):
            while st and heights[st[-1]]>=h:
                height = heights[st.pop()]
                if st:
                    left = st[-1]
                else:
                    left = -1
                best = max(best, height * (i - left -1))
            st.append(i)
        return best