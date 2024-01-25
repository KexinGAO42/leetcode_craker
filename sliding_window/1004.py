"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
"""


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        """
        Intuition
        To find the longest subarray with contiguous 1's we might need to find all the subarrays first.
        But do we really need to do that? If we find all the subarrays we are essentially finding out so many unnecessary overlapping subarrays too.
        We can use a simple sliding window approach to solve this problem.
        The solution is pretty intuitive. We keep expanding the window by moving the right pointer.
        When the window has reached the limit of 0's allowed, we contract (if possible) and save the longest window till now.
        The answer is the longest desirable window.
        """

        left = 0

        for right in range(len(nums)):
            # If we included a zero in the window we reduce the value of k.
            # Since k is the maximum zeros allowed in a window.
            if nums[right] == 0:
                k -= 1
            # A negative k denotes we have consumed all allowed flips and window has
            # more than allowed zeros, thus increment left pointer by 1 to keep the window size same.
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1

        return right - left + 1
