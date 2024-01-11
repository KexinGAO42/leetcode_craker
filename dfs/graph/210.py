"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses.
If there are many valid answers, return any of them.
If it is impossible to finish all courses, return an empty array.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

Example 2:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

Example 3:
Input: numCourses = 1, prerequisites = []
Output: [0]
"""

from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # Intuition: as we've done in the Course Schedule Problem, when we detect a cycle, we cannot finish all courses.
        # In this problems, we also need to return the sequence of the course, so during the dfs, we need to record the track

        # S1: define data structure and variables
        graphmap = defaultdict(list)
        for [cour, preq] in prerequisites:
            graphmap[cour].append(preq)

        visited = [0 for i in range(numCourses)]  # 0 not visited; 1 visited; -1 being visited in the dfs
        self.sequence = []
        self.cycle = False

        # S3: define dfs
        def dfs(courseNumber):
            # define base cases
            if visited[courseNumber] == -1:  # we find a cycle
                self.cycle = True
                return
            if visited[courseNumber] == 1:  # we've visited this course and there's no cycle
                return
            # !! process current node before further dfs
            visited[courseNumber] = -1
            # process neighbors
            for prereq in graphmap[courseNumber]:
                dfs(prereq)
            # !! process current node after finish the dfs
            visited[courseNumber] = 1
            self.sequence.append(courseNumber)

        # S2: define the main function
        for course in range(numCourses):
            dfs(course)
            if self.cycle:
                return []
        return self.sequence
