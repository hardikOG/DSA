class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxWater =0
        left = 0
        n = len(height)
        right = n-1
        while left<right:
            width = right - left
            heightC = min(height[left], height[right])
            curr = heightC * width
            if curr>maxWater:
                maxWater = curr
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return maxWater