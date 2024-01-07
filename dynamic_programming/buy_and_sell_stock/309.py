"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:
After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

Example 2:
Input: prices = [1]
Output: 0
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        :param prices:
        :return:
        """
        # Solution 1: 2-D DP
        # Time Complexity: O(N); Space Complexity: O(N)
        # Step 1: define the state variables
        #   1) price of each day -> prices[1]; 2) stock holding status -> not_hold, hold, cd
        # Step 2: define the memo array
        #   dp[len(prices)][len(3)]
        # Step 3: define the initial values
        #   dp[0][0] = 0
        #   dp[0][1] = -prices[0]
        #   dp[0][2] = 0
        # Step 4: define the state transition functions
        #   dp[i][0] -> not holding stock; compare previous hold and previous CD
        #   dp[i][1] = holding stock; compare previous holding and buying today
        #   dp[i][2] = CD; previous held and selling today

        if len(prices) == 0:
            return 0

        dp = [[0 for i in range(3)] for i in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[0][2] = 0

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            dp[i][2] = dp[i-1][1] + prices[i]

        return max(dp[len(prices)-1][1], dp[len(prices)-1][2])

        # Solution 1 extended: Space complexity O(N) -> O(1)

        if len(prices) == 0:
            return 0

        not_hold = 0
        hold = -prices[0]
        cd = 0

        for i in range(1, len(prices)):
            tmp_not_hold = not_hold
            tmp_hold = hold
            not_hold = max(not_hold, cd)
            hold = max(hold, tmp_not_hold - prices[i])
            cd = tmp_hold + prices[i]

        return max(not_hold, cd)