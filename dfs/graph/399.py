"""
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i].
Each Ai or Bi is a string that represents a single variable.
You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.
Return the answers to all queries. If a single answer cannot be determined, return -1.0.
Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.
Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

Example 1:
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation:
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0

Example 2:
Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]

Example 3:
Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
"""

from collections import defaultdict


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        # Intuition: form the equations into a graph and dfs the equations.

        # !! Special point: we need to start from a source, and reach a target by dfs.
        # In this case, we need to consider the case of we get stuck (cannot reach the target) in the mid of dfs.
        # Solution: define global boolean - if we end with target, set to True; else set to False.
        # Also: to reach the target, we might have multiple paths, so we can early stop when one path is found.

        # S1: define data structures
        output = []
        one_output = []

        direction, result = defaultdict(list), {}
        for i in range(len(values)):
            direction[equations[i][0]].append(equations[i][1])
            direction[equations[i][1]].append(equations[i][0])
            result[(equations[i][0], equations[i][1])] = values[i]
            result[(equations[i][1], equations[i][0])] = 1 / values[i]

        # S3: define dfs
        def dfs(src, tar, tmp):
            # define base case
            if src == tar:
                res = 1.0
                for val in tmp:
                    res *= val
                output.append(res)
                self.found = True
                return
            # process current node
            visited.add(src)
            # process neighbors
            for neighbor in direction[src]:
                if neighbor not in visited:
                    tmp.append(result[(src, neighbor)])
                    dfs(neighbor, tar, tmp)
                    if self.found:
                        return
                    tmp.pop(-1)

        # S2: define main function
        for query in queries:
            self.found = False
            visited = set()
            if query[0] in direction.keys() and query[1] in direction.keys():
                dfs(query[0], query[1], [])
                if not self.found:
                    output.append(-1)
            else:
                output.append(-1)
        return output
