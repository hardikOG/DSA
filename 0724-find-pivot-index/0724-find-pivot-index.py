class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l_s = 0
        total_sum = sum(nums)
        for i, num in enumerate(nums):
            if l_s == (total_sum - l_s- num):
                return i
            l_s += num
        return -1
