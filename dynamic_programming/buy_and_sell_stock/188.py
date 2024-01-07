"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.
Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times and sell at most k times.
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:
Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:
Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
"""


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
        :param k:
        :param prices:
        :return:
        """
        # Step 1: define state variables
        #   1) prices[i]; 2) whether holding the stock or not; 3) number of transaction (k)
        # Step 2: define the memo array
        #   dp[len(prices)][len(2)][len(k+1)]
        # Step 3: define the initial values
        # for all k:
        #   dp[0][0][k] = 0
        #   dp[0][1][k] = -prices[0]
        # Step 4: define the state transition functions
        #   can be generalized from LeetCode #123

        if len(prices) == 0:
            return 0

        if len(prices) == 0:
            return 0

        dp = [[[0 for i in range(k + 1)] for i in range(2)] for i in range(len(prices))]

        for i in range(k + 1):
            dp[0][0][i] = 0
            dp[0][1][i] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0][0] = 0
            for j in range(1, k + 1):
                dp[i][0][j] = max(dp[i - 1][0][j], dp[i - 1][1][j - 1] + prices[i])
            for j in range(k):
                dp[i][1][j] = max(dp[i - 1][1][j], dp[i - 1][0][j] - prices[i])
            dp[i][1][k] = 0

        return dp[len(prices) - 1][0][k]
