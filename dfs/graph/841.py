"""
There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms.
However, you cannot enter a locked room without having its key.
When you visit a room, you may find a set of distinct keys in it.
Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.
Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.

Example 1:
Input: rooms = [[1],[2],[3],[]]
Output: true
Explanation:
We visit room 0 and pick up key 1.
We then visit room 1 and pick up key 2.
We then visit room 2 and pick up key 3.
We then visit room 3.
Since we were able to visit every room, we return true.

Example 2:
Input: rooms = [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.
"""


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        # Intuition: we form the keys and rooms as a directed graph. Keep track of visited room

        # S1: define data structures and variables
        visited = set()
        graphmap = {}
        for i in range(len(rooms)):
            graphmap[i] = rooms[i]

        # S3: define dfs function
        def dfs(room_num):
            # define base case
            if room_num in visited or len(graphmap[room_num]) == 0:
                visited.add(room_num)
                return
            # process neighbors
            for room in graphmap[room_num]:
                visited.add(room_num)
                dfs(room)

        # S2: define main function
        dfs(0)
        if len(visited) == len(rooms):
            return True
        else:
            return False