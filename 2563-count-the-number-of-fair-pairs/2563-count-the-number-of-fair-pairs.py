class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        nums.sort()
        def count(x):
            left = 0
            right = len(nums) - 1
            res = 0
            while left<right:
                if nums[left] + nums[right] <=x:
                    res+= right - left
                    left+=1
                else:
                    right-=1
            return res
        return count(upper) - count(lower-1)