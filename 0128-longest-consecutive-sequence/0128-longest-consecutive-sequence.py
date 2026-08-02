class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0
        seen = set(nums)
        for num in seen:
            if num-1 not in seen:
                length = 1
                while num + length in seen:
                    length +=1
                longest = max(longest, length)
        return longest