class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_len = 1
        curr_len = 1
        dec_len = 1
        for i in range(1, len(nums)):
            if nums[i]>nums[i-1]:
                curr_len+=1
                dec_len =1
            elif nums[i]<nums[i-1]:
                dec_len +=1
                curr_len = 1
            else:
                dec_len =1
                curr_len = 1
            max_len = max(max_len,dec_len, curr_len)
        return max_len