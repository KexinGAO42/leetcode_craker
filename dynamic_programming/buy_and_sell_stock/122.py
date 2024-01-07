"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time.
However, you can buy it then immediately sell it on the same day.
Find and return the maximum profit you can achieve.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.

Example 3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        :param prices: List[int]
        :return: max_profit: int
        """

        # Solution 1: Brute Force Searching ?
        # Traverse through prices:
        #   if prices[i] < prices[i+1], buy at prices[i]
        #       if prices[i+2] >= prices[i+1], hold at prices[i+1]
        #       if prices[i+2] < prices[i+1], sell at prices[i+1]

        # Solution 2: Math proven - always buy if next day's price is higher than today
        # Time complexity: O(n)
        # Space complexity: O(1)
        max_profit = 0
        for i in range(len(prices) - 1):
            if prices[i+1] > prices[i]:
                sub_profit = prices[i+1] - prices[i]
                max_profit += sub_profit
        return max_profit

        # Solution 3: 2-d DP array
        # Step 1: define the state variable
        #   1) prices; 2) hold the stock or not (hold & not hold)
        # Step 2: define the memo array (DP array)
        #   DP[n][2] -> n: prices[i]; 2: 0=not_hold, 1=hold
        # Step 3: define the initial values
        #   dp[0][0] = 0 (not holding stock at prices[0] leads to 0 cost)
        #   dp[0][1] = -prices[0] (holding stock at prices[0] will cost prices[0])
        # Step 4: define the state transition equation (making decision)
        #   dp[i][1] = hold = max(prev_hold, prev_not_hold - crt_price)
        #   hold at this point, the max profit you can get
        #   dp[i][0] = not_hold = max(prev_not_hold, crt_price + prev_hold)
        #   not hold at this point, the max profit you can get
        # Time Complexity: O(N)
        # Space Complexity: O(N)
        dp = [[-inf] * 2] * len(prices)
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            dp[i][0] = max(prices[i] + dp[i-1][1], dp[i-1][0])
        return dp[len(prices) - 1][0]

        # Solution 3 extended: 2 dp constant (Space Complexity: O(N) -> O(1))
        hold, not_hold = -prices[0], 0
        for i in range(1, len(prices)):
            hold = max(hold, not_hold - prices[i])
            not_hold = max(not_hold, hold + prices[i])
        return not_hold
