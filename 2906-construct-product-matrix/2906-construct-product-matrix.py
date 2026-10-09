class Solution(object):
    def constructProductMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        MOD = 12345
        n = len(grid)
        m = len(grid[0])
        flat = []
        for i in range(n):
            for j in range(m):
                flat.append(grid[i][j])
        f = len(flat)
        pre = [1] * f
        suff = [1] * f
        for i in range(1,f):
            pre[i] = (pre[i-1] * flat[i-1]) % MOD
        for i in range(f-2, -1, -1):
            suff[i] =(suff[i+1] * flat[i+1])%MOD
        res = [[1] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                res[i][j] = (pre[i*m + j] * suff[i*m + j]) % MOD
        return res

