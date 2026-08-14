class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        isIslandCount = 0

        if not grid:
            return 0

        def changeLandToWater(grid, i, j):
            if (i < 0 or j < 0 or
                i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0'):
                return

            grid[i][j] = '0'

            changeLandToWater(grid, i + 1, j)
            changeLandToWater(grid, i - 1, j)
            changeLandToWater(grid, i, j + 1)
            changeLandToWater(grid, i, j - 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    isIslandCount += 1
                    changeLandToWater(grid, i, j)

        return isIslandCount