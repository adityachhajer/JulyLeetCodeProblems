class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        k = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 0:
                    continue
                else:
                    if i == 0 or grid[i - 1][j] == 0:
                        k = k + 1
                    if i == len(grid) - 1 or grid[i + 1][j] == 0:
                        k = k + 1
                    if j == 0 or grid[i][j - 1] == 0:
                        k = k + 1
                    if j == len(grid[0]) - 1 or grid[i][j + 1] == 0:
                        k = k + 1

        return k