"""
There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree).
Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.
Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.
This year, there will be a big event in the capital (city 0), and many people want to travel to this city.
Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.
It's guaranteed that each city can reach city 0 after reorder.

Example 1:
Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

Example 2:
Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
Output: 2
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

Example 3:
Input: n = 3, connections = [[1,0],[2,0]]
Output: 0
"""

from collections import defaultdict


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        # Intuition: start from city 0, dfs its neighbor, if the neiborgh points to city 0, no reorder, else reorder += 1

        # S1: define data structures and variables
        forward = defaultdict(list)
        backward = defaultdict(list)
        visited = set()
        self.res = 0

        for [i, j] in connections:
            forward[i].append(j)
            backward[j].append(i)

        # S3: define dfs
        def dfs(city):
            if city in visited:
                return
            # process neighbor
            visited.add(city)
            if city in backward.keys():
                for neighbor in backward[city]:
                    dfs(neighbor)
            if city in forward.keys():
                for neighbor in forward[city]:
                    if neighbor not in visited:
                        self.res += 1
                        dfs(neighbor)
            return

        # S2: define main function
        dfs(0)
        return self.res

