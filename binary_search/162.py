"""
A peak element is an element that is strictly greater than its neighbors.
Given a 0-indexed integer array nums, find a peak element, and return its index.
If the array contains multiple peaks, return the index to any of the peaks.
You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
"""


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        # Intuition: we have to search with tc O(log n), so we need to use Binary Search
        # Recall the key to do Binary Search - define a if condition so that we can map one part as T/F and other part F/T
        # To find peak, we define the if condition by comparing the mid number and the mid+1 number, if mid > mid+1, mid is higher than right, so we go to the left to find the first True point
        # Extension: we have four ways to code: find first True, find first False, find last T, and find last F

        # S1: initialize lowerbound and upperbound
        left, right = 0, len(nums) - 1

        # S2: define while loop
        while left < right:
            # define mid point
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:  # True condition
                right = mid
            else:
                left = mid + 1
        return left
