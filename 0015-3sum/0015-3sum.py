class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i+1
            right = n-1
            
            while left<right: 
                summ = nums[i] + nums[left] + nums[right]
                if summ == 0:
                    res.append([nums[i],nums[left],nums[right]])
                    left+=1
                    while left<right and nums[left] == nums[left-1]:
                        left+=1
                elif summ < 0:
                    left+=1
                else:
                    right-=1
            
        return res