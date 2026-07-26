class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if total%2 != 0:
            return False
        target = total // 2
        n = len(nums)
        dp = [[False] * (target+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = True
        for i in range(1, n+1):
            for j in range(1, target+1):
                if nums[i-1]<=j:
                    include = dp[i-1][j- nums[i-1]]
                    exclude = dp[i-1][j]  #take prev value
                    dp[i][j] = include or exclude
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][target]