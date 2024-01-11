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

        Intuition: the prereqs can form a directed graph; if there is a loop in the graph, we cannot finish all courses
        !! The way to find a cycle:
        we give a course 3 status: not visited; visited; being visited
        data structure - list of len(numCourses) 0 not visited; 1 visited, -1 being visited

        data structure - graph: dict[prereq] = [courses]
        dfs:
        - target: find a loop
        - input: starting node; visited list; resolved set
        """

        # S1: Represent the courses and prerequisites using a graph (adjacency list)
        graph = [[] for _ in range(numCourses)]
        for prerequisite in prerequisites:
            course, pre = prerequisite
            graph[course].append(pre)

        visited = [0 for i in range(numCourses)]

        # S2: Define dfs
        def dfs(course):
            # define base cases:
            if visited[course] == -1:  # The course is being visited in the dfs
                return True
            if visited[course] == 1:  # The course is already visited and there is no cycle
                return False
            # !! process current node: before we go into deeper dfs, mark as being visited
            visited[course] = -1
            # process neighbors
            for pre in graph[course]:
                if dfs(pre):
                    return True  # Cycle detected in the subtree
            # !! process current node: after we get out from dfs, mark as visited
            visited[course] = 1  # Mark as visited
            return False

        # S3: define main function
        for course in range(numCourses):
            if not visited[course] and dfs(course):
                return False  # Cycle detected, cannot finish all courses

        return True  # No cycle detected, can finish all courses



