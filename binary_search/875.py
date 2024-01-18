"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas.
The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k.
Each hour, she chooses some pile of bananas and eats k bananas from that pile.
If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:
Input: piles = [30,11,23,4,20], h = 6
Output: 23
"""


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Intuition:
        # We need to search the minimum speed k, to ensure koko finishes eating within h.
        # From the example, we can see that k will range from 1 to max[piles].
        # Intuively, we can use binary search, because we can form a if condition to split the array into F/T.
        # The if condition: with speed k, we want sum(math.ceil(pile / speed)) <= h

        def canFinish(speed):
            time = sum(math.ceil(pile / speed) for pile in piles)
            return time <= h  # True condition

        left, right = 1, max(piles)
        mid = left + (right - left) // 2
        while left <= right:
            if canFinish(mid):  # find the first True
                right = mid - 1
            else:
                left = mid + 1
            mid = left + (right - left) // 2
        return right + 1
