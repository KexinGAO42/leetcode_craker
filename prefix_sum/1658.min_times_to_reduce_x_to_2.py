"""
You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.



Example 1:

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
Example 2:

Input: nums = [5,6,7,8,9], x = 4
Output: -1
Example 3:

Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.
"""


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        if nums[0] > x and nums[-1] > x:
            return -1
        if sum(nums) < x:
            return -1

        l, r = {}, {}
        l_prefix, r_prefix = 0, 0
        for i in range(len(nums)):
            if l_prefix + nums[i] > x:
                break
            else:
                l_prefix += nums[i]
                l[l_prefix] = i

        for i in range(len(nums) - 1, -1, -1):
            if r_prefix + nums[i] > x:
                break
            else:
                r_prefix += nums[i]
                r[r_prefix] = len(nums) - i - 1

        res = inf
        if x in r.keys():
            res = min(res, r[x] + 1)
        if x in l.keys():
            res = min(res, l[x] + 1)

        for prefix in l.keys():
            if (x - prefix) in r.keys():
                res = min(res, r[x - prefix] + l[prefix] + 2)
        if res == inf:
            return -1
        return res

