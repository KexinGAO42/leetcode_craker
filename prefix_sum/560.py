"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # Intuition:
        # Brute Force solution: O(N^2) traverse i from 0 to len(nums) - 1, traverse j from 1 to len(nums), calculate the sum_nums[i:j] to see whether it's equal to k
        # From the Brute Force solution, we see that the key is sum_nums[i:j], so we know we want to use prefix_sum
        # Let prefix_sum array = F[0, a1, a1+a2, a1+a2+a3, ...]
        # We want F[j] - F[i] == k
        # Which is F[i] == F[j] - k
        # We store F[i] in a hashmap, where key is F[i], and the value is frequency
        # Traverse through nums to calculate F[j] - k

        ans = 0
        prefix_sum = 0
        hashmap = {}
        hashmap[0] = 1

        for num in nums:
            prefix_sum += num
            if prefix_sum - k in hashmap:
                ans += hashmap[prefix_sum - k]
            if prefix_sum not in hashmap:
                hashmap[prefix_sum] = 1
            else:
                hashmap[prefix_sum] += 1
        return ans
