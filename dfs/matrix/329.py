"""
Given an m x n integers matrix, return the length of the longest increasing path in matrix.
From each cell, you can either move in four directions: left, right, up, or down.
You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

Example 1:
Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:
Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

Example 3:
Input: matrix = [[1]]
Output: 1
"""

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        # Intuition:
        # start from each cell, find larger number in neighbors and count (recursively do this until fail - DFS)
        # one cell might be visited more than once, so we want to keep a memo to avoid redundant calculation (dict)

        # S1: initialize variables and data structures
        memo = {}  # key - index of cell (tuple); value - length of longest path (value)

        m, n = len(matrix), len(matrix[0])
        ans = 0

        def dfs(i, j):
            # target: traverse through the increasing paths and record the max length starting from each cell
            if (i, j) in memo.keys():
                return memo[(i, j)]

            res = 0

            dirns = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for (x, y) in dirns:
                ii, jj = i + x, j + y
                if ii >= 0 and jj >= 0 and ii < m and jj < n and matrix[ii][jj] > matrix[i][j]:
                    tmp = dfs(ii, jj)
                    res = max(res, tmp)

            memo[(i, j)] = res + 1
            return res + 1

        for i in range(m):
            for j in range(n):
                cnt = dfs(i, j)
                ans = max(ans, cnt)

        return ans