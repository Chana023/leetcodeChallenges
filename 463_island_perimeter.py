# https://leetcode.com/problems/island-perimeter/description/

class Solution():
    def islandPerimeter(self, grid):
        n = len(grid)
        m = len(grid[0])
        perimeter = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if (j > 0 and grid[i][j - 1] == 0) or j == 0:
                        perimeter = perimeter + 1

                    if (i > 0 and grid[i - 1][j] == 0) or i == 0:
                        perimeter = perimeter + 1

                    if (j < m - 1 and grid[i][j + 1] == 0) or j == m - 1:
                        perimeter = perimeter + 1

                    if (i < n - 1 and grid[i + 1][j] == 0) or i == n - 1:
                        perimeter = perimeter + 1

        print(perimeter)
        return perimeter


sol = Solution()
sol.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])