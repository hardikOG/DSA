class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        a=0
        b=max(nums)
        for i in range(k):
            a+=b
            b+=1    
        return a