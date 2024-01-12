"""
You are given an m x n grid where each cell can have one of three values:
0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange.
If this is impossible, return -1.

Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
"""

from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        num_mins = 0

        # Initialize a queue and the starting node
        queue = deque()
        # Initialize the visited set
        visited = set()
        num_oranges = 0

        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                    visited.add((i, j))
                    num_oranges += 1
                if grid[i][j] == 1:
                    num_oranges += 1

        # While loop
        while queue:
            size = len(queue)
            for i in range(size):

                # dequeue a nodde from the left
                current_node = queue.popleft()

                # enqueue neiborghs
                dirns = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for dirn in dirns:
                    r, c = current_node[0] + dirn[0], current_node[1] + dirn[1]
                    if r >= 0 and c >= 0 and r < m and c < n and (r, c) not in visited and grid[r][c] == 1:
                        visited.add((r, c))
                        queue.append((r, c))
            num_mins += 1

        if num_oranges == 0:
            return 0
        if num_oranges > len(visited):
            return -1
        return num_mins - 1