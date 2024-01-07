"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
1 <= prices.length <= 105
0 <= prices[i] <= 104
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        :param prices: list[int]
        :return: max_profit[int]
        """

        # Solution 1: Brute force search
        # For each day in the price list, get the maximum price in the days after
        # Time Complexity: O(N^2)?
        # Space Complexity: O(1)
        max_profit = 0
        for i in range(len(prices)):
            buy = prices[i]
            sell = max(prices[i:])
            profit = sell - buy
            max_profit = max(profit, max_profit)
        return max_profit

        # Solution 2: 1-d DP
        # In solution 1, there are lots of redundant calculation in sell = max(prices[i:]).
        # Therefore, we create a DP array (dp) to store the maximum price AFTER day[i], where dp[i] = max(prices[i:])
        # Example:
        # prices = [7,1,5,3,6,4]
        # dp = [6,6,6,6,4]
        # Time complexity: O(n)
        # Space complexity: O(n)
        dp = [-1 for i in range(len(prices) - 1)]  # 1. len(dp) = len(prices)-1; 2. initiate with -1 because price>0
        max_price = prices[-1]  # dp[-1] = prices[-1], set it as the first max_price
        for i in range(len(prices) - 2, -1, -1):  # IMPORTANT: go back through the prices list to get dp in one traversal
            max_price = max(prices[i], max_price)
            dp[i] = max_price

        max_profit = 0
        for i in range(len(prices)):
            buy = prices[i]
            sell = dp[i]
            profit = sell - buy
            max_profit = max(profit, max_profit)
        return max_profit

        # Solution 2: 1-d DP extended (Space Complexity O(N)-> O(1))
        # Instead of creating a DP array storing the maximum price AFTER day[i], we store the minimum buying price
        # When traverse through the price, we:
        #   1) check whether the buying price is the lowest till now;
        #   2) calculate the profit and compare with max_profit
        max_profit, buy = -1, inf
        for i in range(len(prices)):
            buy = min(prices[i], buy)
            profit = prices[i] - buy
            max_profit = max(profit, max_profit)
        return max_profit

