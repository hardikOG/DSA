class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(0, len(nums)):
            if nums[i] == 0:
                j = i + 1

                while j < len(nums) and nums[j] == 0:
                    j += 1

                if j < len(nums):
                    nums[i] = nums[j]
                    nums[j] = 0
        return nums