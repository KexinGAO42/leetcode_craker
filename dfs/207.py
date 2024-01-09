"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        input: int; list of lists
        output: boolean

        intuition: the prereqs can form a directed graph; if there is a loop, return False, else True

        data structure - graph: dict[prereq] = [courses]
        dfs:
        - target: find a loop
        - input: starting node; visited set; resolved set
        """

        # Represent the courses and prerequisites using a graph (adjacency list)
        graph = [[] for _ in range(numCourses)]
        for prerequisite in prerequisites:
            course, pre = prerequisite
            graph[course].append(pre)

        visited = [0] * numCourses  # 0: not visited, 1: visited, -1: being visited

        def hasCycle(course):
            if visited[course] == -1:
                return True  # Cycle detected
            if visited[course] == 1:
                return False  # Already visited, no cycle

            visited[course] = -1  # Mark as being visited

            for pre in graph[course]:
                if hasCycle(pre):
                    return True  # Cycle detected in the subtree

            visited[course] = 1  # Mark as visited
            return False

        # Check for cycles in the graph
        for course in range(numCourses):
            if not visited[course] and hasCycle(course):
                return False  # Cycle detected, cannot finish all courses

        return True  # No cycle detected, can finish all courses
