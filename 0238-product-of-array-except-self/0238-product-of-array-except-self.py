class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []
        n = len(nums)
        res = [1] * n
        running_prod = 1
        for i in range(n):
            res[i] = running_prod
            running_prod *= nums[i]
        suffix = 1
        for i in range(n-1,-1,-1):
            res[i] *= suffix
            suffix *= nums[i]
        return res