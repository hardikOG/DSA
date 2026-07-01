class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height)-1
        best = 0
        while left<right:
            width = right - left
            current_area = min(height[left], height[right]) * width
            best = max(best, current_area)
            if height[right]>height[left]:
                left+=1
            else:
                right-=1
        return best