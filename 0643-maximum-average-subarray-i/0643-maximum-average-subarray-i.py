class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        if k>n or k==0:
            return 0
        start = 0
        max_avg = float('-inf')
        window_state = 0
        for end in range(n):
            window_state += nums[end]
            if (end-start+1) == k:
                max_avg = max(max_avg, window_state)
                window_state -= nums[start]
                start+=1
        return float(max_avg)/k
