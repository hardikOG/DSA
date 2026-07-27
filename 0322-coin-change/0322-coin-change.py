class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        n = len(coins)
        INF = float('inf')
        dp = [[INF] * (amount + 1) for _ in range(n+1)]
        
        for i in range(1,n+1):
            dp[i][0] = 0
            for j in range(1,amount + 1):
                dp[i][j] = dp[i-1][j]
                if coins[i-1]<=j:
                    include = 1+ dp[i][j-coins[i-1]] 
                    exclude = dp[i-1][j]
                    dp[i][j] = min(include, exclude)
        return -1 if dp[n][amount] == INF else dp[n][amount]