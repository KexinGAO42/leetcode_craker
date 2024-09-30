"""
Given an integer array nums, you need to find one continuous subarray such that if you only sort this subarray in non-decreasing order, then the whole array will be sorted in non-decreasing order.

Return the shortest such subarray and output its length.

Example 1:

Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Example 2:

Input: nums = [1,2,3,4]
Output: 0
Example 3:

Input: nums = [1]
Output: 0
"""


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # general cases
        """
        Intuition: left and right pointers => get two monotonic stacks
        1. left pointer goes rightward to the tail (On)
            if monotonically increase: push stack
            if not: pop stack
            => we will get a stack of indeces where the nums monotonically increase
            => the first uncontinuos indeces will be the left boundary
        2. right pointer goes leftward to the head (On)
            if monotonically decrease: push stack
            if not: pop stack
        """
        l_stack, r_stack = [], []
        l_pointer, r_pointer = 0, len(nums) - 1
        l_boundary, r_boundary = len(nums) - 1, 0
        while l_pointer < len(nums):
            while l_stack and nums[l_stack[-1]] > nums[l_pointer]:  # decrease
                l_boundary = min(l_boundary, l_stack.pop())
            l_stack.append(l_pointer)
            l_pointer += 1
        while r_pointer >= 0:
            while r_stack and nums[r_stack[-1]] < nums[r_pointer]:  # increase
                r_boundary = max(r_boundary, r_stack.pop())
            r_stack.append(r_pointer)
            r_pointer -= 1

        if r_boundary > l_boundary:
            return r_boundary - l_boundary + 1
        return 0

