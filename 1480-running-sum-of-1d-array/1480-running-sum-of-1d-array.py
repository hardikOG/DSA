class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = [0] * (len(nums)+1)
        for i in range(len(nums)):
            prefix[i+1] = prefix[i] + nums[i]
        return prefix[1:]