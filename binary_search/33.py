"""
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Intuition: we have to search with tc O(log n), so we need to use Binary Search
        # Recall the key to do Binary Search - define a if condition so that we can map one part as T/F and other part F/T
        # When breaking rotated sorted array into two half, we know that one half will be sorted and the other half not by compraing the mid number to the leftmost number. Therefore, we can do BS based on this if condition.

        # S1: initialize the l and r pointers
        left, right = 0, len(nums) - 1

        # S2: while loop
        while left <= right:
            # define mid point
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]:  # the left part is sorted
                if nums[left] <= target < nums[mid]:  # the target is in left
                    right = mid - 1
                else:  # the target is in right
                    left = mid + 1
            else:  # the right part is sorted
                if nums[mid] < target <= nums[right]:  # the target is in right
                    left = mid + 1
                else:  # the target is in left
                    right = mid - 1
        return -1
