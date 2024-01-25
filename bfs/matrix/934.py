"""
You are given an n x n binary matrix grid where 1 represents land and 0 represents water.
An island is a 4-directionally connected group of 1's not connected to any other 1's.
There are exactly two islands in grid.
You may change 0's to 1's to connect the two islands to form one island.
Return the smallest number of 0's you must flip to connect the two islands.

Example 1:
Input: grid = [[0,1],[1,0]]
Output: 1

Example 2:
Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2

Example 3:
Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
"""


from collections import deque


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        # Intuition: this is a question of finding shortest path, so BFS comes to our mind
        # Firstly, we want to identify the first island through BFS travrsal
        # Secondly, we want another BFS starting from the island 1 to get into the water and reach island 2

        # S1: identify the first island
        start_row, start_col = -1, -1
        n = len(grid)
        dirns = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    start_row, start_col = i, j
                    break

        queue_1 = deque([(start_row, start_col)])
        queue_2 = deque([(start_row, start_col)])

        while queue_1:
            (crt_i, crt_j) = queue_1.popleft()
            grid[crt_i][crt_j] = 2
            for (ii, jj) in dirns:
                nxt_i, nxt_j = ii + crt_i, jj + crt_j
                if 0 <= nxt_i < n and 0 <= nxt_j < n and grid[nxt_i][nxt_j] == 1:
                    queue_1.append((nxt_i, nxt_j))
                    queue_2.append((nxt_i, nxt_j))
                    grid[nxt_i][nxt_j] = 2

        # S2: traverse the water

        distance = 0
        while queue_2:
            crt_level_len = len(queue_2)
            for i in range(crt_level_len):
                (crt_i, crt_j) = queue_2.popleft()
                for (ii, jj) in dirns:
                    nxt_i, nxt_j = ii + crt_i, jj + crt_j
                    if 0 <= nxt_i < n and 0 <= nxt_j < n:
                        if grid[nxt_i][nxt_j] == 0:
                            queue_2.append((nxt_i, nxt_j))
                            grid[nxt_i][nxt_j] = -1
                        if grid[nxt_i][nxt_j] == 1:
                            return distance
            distance += 1
