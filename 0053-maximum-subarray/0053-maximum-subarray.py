class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        n = len(nums)
        max_sum = float('-inf')
        window_sum = 0
        for right in range(n):
            window_sum += nums[right]
            max_sum = max(max_sum , window_sum)
            if window_sum < 0:
                window_sum = 0
                left = right + 1
        return max_sum