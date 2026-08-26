class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        n = len(nums)
        for i in range(n-1,-1,-1):
            num = nums[i]
            freq[num] = freq.get(num, 0) + 1
            if freq[num] > 2:
                del nums[i]
        return len(nums)

