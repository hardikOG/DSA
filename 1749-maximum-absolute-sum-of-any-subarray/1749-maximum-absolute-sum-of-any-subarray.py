class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = 0
        pos_window = 0
        neg_window =0
        n = len(nums)
        left = 0
        for right in range(n):
            pos_window += nums[right]
            neg_window += nums[right]
            if pos_window < 0:
                pos_window = 0
                left = right + 1
            if neg_window > 0:
                neg_window = 0
                left = right + 1
            max_sum = max(max_sum, abs(pos_window), abs(neg_window))
        return max_sum