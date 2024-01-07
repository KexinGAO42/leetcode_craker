"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.
The only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        :param nums:
        :return:
        """
        # S1: Define the state variables
        #   1) money of each house (nums[i]); 2) can be robbed or not (0, 1)
        # S2: Define the memo array
        #   dp[i] of len(nums): at house_i, the maximum money we can rob
        # S3: Define the initial values
        #   dp[0] = 0
        #   dp[1] = max(nums[0], nums[1])
        # S4: Define the state transition functions
        #   not robbing at house i -> can rob from dp[0] -> dp[i-1]
        #   robbing at house i -> can rob from dp[0] -> dp[i-2]
        #   we want to max(dp[i-1], dp[i-2]+nums[i])

        if len(nums) == 0:
            return 0

        dp = [0 for i in range(len(nums))]

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[i]