"""
Given an integer array nums and an integer k, return the maximum length of a subarray that sums to k.
If there is not one, return 0 instead.

Example 1:
Input: nums = [1,-1,5,-2,3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.

Example 2:
Input: nums = [-2,-1,2,1], k = 1
Output: 2
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
"""

"""
Intuition:

1. Use Prefix Sum:
As we iterate through the array, maintain a running sum called prefix_sum. 
At any index i, the prefix_sum represents the sum of all elements from the start of the array to the current index.

2. Use a Hash Map:
Store each prefix_sum along with its index in a hash map. 
This helps us quickly check if there exists a previous index where the prefix_sum was prefix_sum - k. 
If such a prefix sum exists, the subarray between that previous index and the current index has a sum of k.

3. Check for Subarray:
For each element in the array, calculate the current prefix_sum and check if prefix_sum - k exists in the hash map. 
If it does, this means there is a subarray that sums to k, and the length of this subarray is the difference between the current index and the index where prefix_sum - k occurred.

4. Track the Maximum Subarray Length:
Keep a variable to track the maximum length of such subarrays as you find them.

5. Edge Case:
Initialize the hash map with prefix_sum = 0 at index -1 to handle cases where a subarray from the start of the array sums to k.
"""


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        indeces = {0: -1}
        res = 0
        prefix = 0
        for i, num in enumerate(nums):
            prefix += num
            if prefix not in indeces.keys():
                indeces[prefix] = i
            if (prefix - k) in indeces.keys():
                res = max(res, i - indeces[prefix - k])
        return res
