"""
You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+').
You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.
In one step, you can move one cell up, down, left, or right.
You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance.
An exit is defined as an empty cell that is at the border of the maze.
The entrance does not count as an exit.
Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

Example 1:
Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
Output: 1
Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
Initially, you are at the entrance cell [1,2].
- You can reach [1,0] by moving 2 steps left.
- You can reach [0,2] by moving 1 step up.
It is impossible to reach [2,3] from the entrance.
Thus, the nearest exit is [0,2], which is 1 step away.

Example 2:
Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
Output: 2
Explanation: There is 1 exit in this maze at [1,2].
[1,0] does not count as an exit since it is the entrance cell.
Initially, you are at the entrance cell [1,0].
- You can reach [1,2] by moving 2 steps right.
Thus, the nearest exit is [1,2], which is 2 steps away.

Example 3:
Input: maze = [[".","+"]], entrance = [0,0]
Output: -1
Explanation: There are no exits in this maze.
"""


from collections import deque


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        # Intuition:
        # We want to find a shortest path in a matrix, so we consider BFS
        # Ending condition: reach an empty cell which is at the border

        # S1: define variables
        row, col = len(maze), len(maze[0])
        dirns = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        start_row, start_col = entrance
        maze[start_row][start_col] = "+"
        queue = collections.deque()
        queue.append([start_row, start_col, 0])

        # S2: define bfs
        while queue:
            # get current cell
            crt_r, crt_c, cur_step = queue.popleft()
            # get all possible neighbors (only when the crt is not at the boarder)
            for dirn in dirns:
                i, j = crt_r + dirn[0], crt_c + dirn[1]
                # check whether the dirn is possible
                if 0 <= i < row and 0 <= j < col and maze[i][j] == ".":
                    # check whether the cell is an exit
                    if i == 0 or i == row - 1 or j == 0 or j == col - 1:
                        return cur_step + 1
                    maze[i][j] = "+"
                    queue.append([i, j, cur_step + 1])

        return -1
