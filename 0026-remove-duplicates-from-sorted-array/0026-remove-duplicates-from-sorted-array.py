class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        i = 0
        while i<len(nums):
            if nums[i] in seen:
                del nums[i]
            else:
                seen.add(nums[i])
                i+=1
        return len(nums)