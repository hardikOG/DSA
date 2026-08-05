class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [-1] *n
        stack = []
        for i in range(2*n):
            idx = i%n   #maps the second traversal back onto the real indices
            while stack and nums[stack[-1]] < nums[idx]:
                res[stack.pop()] = nums[idx]
            if i<n:
                stack.append(idx)
        return res