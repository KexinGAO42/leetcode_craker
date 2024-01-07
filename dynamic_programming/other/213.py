"""
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle.
That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:
Input: nums = [1,2,3]
Output: 3
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        :param nums:
        :return:
        """

        # Based on #198, this problem adds a constraint:
        #   1) if you rob the first house, you can only rob house[0] -> house[-2]
        #   2) if you rob the last house, you can only rob house[1] -> house[-1]
        # Therefore, we turn this question into two #198 based on the two conditions

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        # Condition 1: rob the first house

        nums1 = nums[:-1]
        dp1 = [0 for i in range(len(nums1-1))]
        dp1[0], dp1[1] = nums[0], nums[0]

        for i in range(2, len(nums1)):
            dp1[i] = max(dp1[i-1], dp1[i-2] + nums1[i])

        res1 = dp1[len(nums1)-1]

        # Condition 2: rob at the last house

        nums2 = nums[1:]
        dp2 = [0 for i in range((len(nums2-1)))]
        dp2[0], dp2[1] = nums2[0], max(nums2[0], nums2[1])

        for i in range(2, len(nums2)):
            dp2[i] = max(dp2[i-1], dp2[i-2] + nums2[i])

        if dp2[-1] == dp2[-2]:
            res2 = dp2[len(nums2)-1] + nums[0]
        else:
            res2 = dp2[len(nums2)-1]

        return max(res1, res2)



