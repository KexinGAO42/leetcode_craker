"""
You are given an m x n grid rooms initialized with these three possible values.
-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example 1:
Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

Example 2:
Input: rooms = [[-1]]
Output: [[-1]]
"""

from collections import deque


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        # Intuition: we want to find the shortest path from a room to a gate, so we can use BFS
        # starting from each gate, we BFS its possible neiborgh (not a wall, inside the grid, unvisited), mark the number

        queue = deque()
        row, col = len(rooms), len(rooms[0])
        dirns = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        for i in range(row):
            for j in range(col):
                if rooms[i][j] == 0:
                    queue.append((i, j))

        level = 1
        while queue:
            crt_level_len = len(queue)
            for i in range(crt_level_len):
                crt_cell = queue.popleft()
                for [ii, jj] in dirns:
                    nxt_row, nxt_col = crt_cell[0] + ii, crt_cell[1] + jj
                    if 0 <= nxt_row < row and 0 <= nxt_col < col:
                        if rooms[nxt_row][nxt_col] == 2147483647:
                            rooms[nxt_row][nxt_col] = level
                            queue.append((nxt_row, nxt_col))
            level += 1
