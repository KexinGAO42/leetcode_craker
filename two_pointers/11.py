"""
You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:

        # Intuition: we need to move two pointers and calculate the amount of water, it seems to be a 2-pointers problem
        # the amount of water = min(height[p2], height[p1]) * (p2 - p1)
        # since every time we move p1 or p2, (p2 - p1) decreases, so we want to make sure min(height[p2], height[p1]) increases
        # that means, we need to move the lower point to find one that is higher

        left, right = 0, len(height) - 1
        ans = min(height[left], height[right]) * right

        while left < right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            ans = max(min(height[left], height[right]) * (right - left), ans)

        return ans
