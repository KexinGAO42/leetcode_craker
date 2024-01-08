"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # Solution 1: DFS
        # Recursion (helper function)：Recursively visit each grid with "1", to see whether it can move to aother
        # Memo/visited (set): save the visited grids so that we won't visit them again

        if not grid:
            return 0

        row, col = len(grid), len(grid[0])
        visited = set()
        count = 0

        # Step 1: Define the main function so that we can clearly know what we want the dfs do
        for i in range(row):
            for j in range(col):
                if (i, j) not in visited and grid[i][j] == "1":
                    dfs(i, j, visited)
                    count += 1

        # Step 2: Define the helper function (DFS)
        def dfs(i, j, visited):

            # Step 2.1: When there is a DFS, we first decide the return condition
            if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] == "0" or (i, j) in visited:
                return
            # Step 2.2: We keep visited cell in the set
            visited.add((i, j))
            # Step 2.3: Define the recursive part
            dirns = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dirn in dirns:
                ii, jj = i + dirn[0], j + dirn[1]
                dfs(ii, jj, visited)

        return count
