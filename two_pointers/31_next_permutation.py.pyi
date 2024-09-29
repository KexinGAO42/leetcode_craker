"""
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
"""


"""
We need to find the next larger permutation by making a minimal change to the current sequence. 
We need to identify the first position where we can swap two numbers to make the sequence larger, but only by a small margin.
1. Find the first decreasing element nums[i]
2. Find the smallest larger element nums[j]
3. Swap nums[i] and nums[j]
4. Reverse the tail
"""


class Solution:
    # define a function that swaps two numbers
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    # define a function that reverse the numbers in [start, len(nums) - 1] from mono decre to mono incre
    def reverse(self, nums, start):
        i, j = start, len(nums) - 1
        while i < j:
            self.swap(nums, i, j)
            i += 1
            j -= 1

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        1. start from the right side, go leftwards, check if it's monotonic increasing
        2. once we find a point where it starts to decrease:
            a. anchor this number
            b. from the number, we go rightwards, find the smallese number that is larger than the anchored number
            c. swap the number
            d. reverse all numbers after the anchored point
        """

        # check the nums from right to left
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:  # when the while loop breaks, we get the anchor index (i) to swap
            i -= 1

        if i >= 0:  # go back left and find the smallest number greater than nums[i - 1]
            j = i + 1
            while j < len(nums) and nums[j] > nums[
                i]:  # when the while loop breaks, we get another anchor index (j - 1) to swap
                j += 1
            self.swap(nums, i, j - 1)
        self.reverse(nums, i + 1)
