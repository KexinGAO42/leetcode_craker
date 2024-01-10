"""
There are n cities. Some of them are connected, while some are not.
If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
A province is a group of directly or indirectly connected cities and no other cities outside of the group.
You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
Return the total number of provinces.

Example 1:
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Example 2:
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
"""

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        # Intuition:
        # DFS: for each city recursively visit its connected cities and put them in visited set;
        # when finish a visit, province += 1

        # S1: define variables
        visited = set()
        num_city = len(isConnected)
        num_province = 0
        connection = {}
        for i in range(num_city):
            connection[i] = []
            for j in range(num_city):
                if i != j and isConnected[i][j] == 1:
                    connection[i].append(j)

        # S3: define dfs
        def dfs(city):
            # define base case
            if city in visited:
                return
            # process neiborghs
            visited.add(city)
            for neiborgh in connection[city]:
                dfs(neiborgh)

        # S2: define main function
        for i in range(num_city):
            if len(connection[i]) == 0:
                visited.add(i)
                num_province += 1
            else:
                if i not in visited:
                    dfs(i)
                    num_province += 1

        return num_province
