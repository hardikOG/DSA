class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        need = {}
        for i,num in enumerate(nums):
            compl = target - num
            if compl in need:
                return [need[compl],i]
            need[num] = i