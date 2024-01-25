"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0
"""


from collections import deque


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # Intuition: by translating "the fewest number of coins that you need to make up that amount", we see it's actually to find the shortest path. So we can use BFS.
        # when we use BFS you don't have to think about the minimum: the first found number of coins will be the answer.

        if amount == 0:
            return 0

        # enqueue the target amount and the number of coins
        queue = deque([(amount, 0)])
        # initialze visited set to avoid redundant process
        visited = set()

        while queue:
            cur_amount, crt_cnt = queue.popleft()

            if cur_amount == 0:
                return crt_cnt

            for coin in coins:
                new_amount = cur_amount - coin
                # if we've already checked this amount or amount smaller than zero, stop searching this path
                if new_amount in visited or new_amount < 0:
                    continue
                queue.append((new_amount, crt_cnt + 1))
                visited.add(new_amount)

        return -1
