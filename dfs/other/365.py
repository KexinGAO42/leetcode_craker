"""
You are given two jugs with capacities jug1Capacity and jug2Capacity liters.
There is an infinite amount of water supply available.
Determine whether it is possible to measure exactly targetCapacity liters using these two jugs.
If targetCapacity liters of water are measurable, you must have targetCapacity liters of water contained within one or both buckets by the end.

Operations allowed:
Fill any of the jugs with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full, or the first jug itself is empty.

Example 1:
Input: jug1Capacity = 3, jug2Capacity = 5, targetCapacity = 4
Output: true
Explanation: The famous Die Hard example

Example 2:
Input: jug1Capacity = 2, jug2Capacity = 6, targetCapacity = 5
Output: false

Example 3:
Input: jug1Capacity = 1, jug2Capacity = 2, targetCapacity = 3
Output: true
"""


class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:

        # Intuition:
        # We have four operation: +jug1, -jug1, +jug2, -jug2
        # We want combine some operations above to form a total value
        # We want to search for a total == target

        # S1: define variables
        reached = set()
        total = 0
        ops = [jug1Capacity, jug2Capacity, -jug1Capacity, -jug2Capacity]
        self.res = False

        # S3: define dfs
        def dfs(total):
            # define base case (physically, we can not have capacity < 0 or capacity > jug1 + jug2):
            if total < 0 or total > jug1Capacity + jug2Capacity or total in reached:
                return
            if total == targetCapacity:
                self.res = True
                return
            # process neighbor
            reached.add(total)
            for op in ops:
                dfs(total + op)

        # S2: define main function
        dfs(total)

        return self.res