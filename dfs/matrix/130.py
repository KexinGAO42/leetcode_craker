"""
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example 1:
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.

Example 2:
Input: board = [["X"]]
Output: [["X"]]
"""


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # Intuition: Similar to the Number of Ilands problem, we want to find all connected "O" as a region and flip it;
        # but note that if this region reaches the border of the matrix, we don't flip it
        # From each cell with "O", we dfs its neighbors to find and mark the region.
        # If no cell in the region at the border, we flip it.

        # S1: define variables
        visited = set()
        m, n = len(board), len(board[0])

        # S3: define dfs
        def dfs(i, j):
            # define base case
            if i < 0 or j < 0 or i >= m or j >= n or board[i][j] == "X" or (i, j) in visited:
                return
            # process current node
            visited.add((i, j))
            self.region.add((i, j))
            if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                self.captured = False
            # process neighbors
            dirns = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dirn in dirns:
                ii, jj = i + dirn[0], j + dirn[1]
                dfs(ii, jj)

        # S2: define the main function
        for i in range(m):
            for j in range(n):
                self.captured = True
                self.region = set()
                if board[i][j] == "O" and (i, j) not in visited:
                    dfs(i, j)
                    if self.captured:
                        for (x, y) in self.region:
                            board[x][y] = "X"