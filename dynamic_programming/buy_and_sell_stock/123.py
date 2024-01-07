"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
Find the maximum profit you can achieve. You may complete at most two transactions.
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.

Example 3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        :param prices: prices list
        :return: max_profit: int
        """

        # Step 1: define the state variables:
        #   1) price at each day -> prices[i] (len(prices))
        #   2) hold the stock or not (0, 1)
        #   3) number of transaction -> no more than 2 (0, 1, 2)
        # Step 2: define the memo array:
        #   dp[len(prices)][len(2)][len(3)]
        # Step 3: define the initial values:
        #   not holding: not buying at day_0
        #       dp[0][0][0] = 0
        #       dp[0][0][1] = 0
        #       dp[0][0][2] = 0
        #   holding: buying at day_0
        #       dp[0][1][0] = -prices[0]
        #       dp[0][1][1] = -prices[0]
        #       dp[0][1][2] = -prices[0]
        # Step 4: define the state transition functions
        #   dp[i][0][0] = 0 -> if not holding at day_i and have sold 0 times, profit would be zero
        #   dp[i][0][1] -> not holding, have sold once; 1) i-1 not hold; 2) i-1 hold, i sell
        #   dp[i][0][2] -> not holding, have sold twice; 1) i-1 not hold; 2) i-1 hold, i sell
        #   dp[i][1][0] -> holding, have sold 0 time; 1) i-1 hold; 2) i-1 not hold, i buy
        #   dp[i][1][1] -> holding, have sold once; 1) i-1 hold; 2) i-1 not hold, i buy
        #   dp[i][0][2] = 0 -> not influencing anything

        dp = [[[int for i in range(3)] for i in range(2)] for i in range(len(prices))]

        dp[0][0][0], dp[0][0][1], dp[0][0][2] = 0, 0, 0
        dp[0][1][0], dp[0][1][1], dp[0][1][2] = -prices[0], -prices[0], -prices[0]

        for i in range(1, len(prices)):
            dp[i][0][0] = 0
            dp[i][0][1] = max(dp[i-1][0][1], dp[i-1][1][0] + prices[i])
            dp[i][0][2] = max(dp[i-1][0][2], dp[i-1][1][1] + prices[i])
            dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][0][0] - prices[i])
            dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][0][1] - prices[i])
            dp[i][1][2] = 0

        return dp[len(prices)-1][0][2]




