"""
You are given the customer visit log of a shop represented by a 0-indexed string customers consisting only of characters 'N' and 'Y':
if the ith character is 'Y', it means that customers come at the ith hour
whereas 'N' indicates that no customers come at the ith hour.
If the shop closes at the jth hour (0 <= j <= n), the penalty is calculated as follows:
For every hour when the shop is open and no customers come, the penalty increases by 1.
For every hour when the shop is closed and customers come, the penalty increases by 1.
Return the earliest hour at which the shop must be closed to incur a minimum penalty.
Note that if a shop closes at the jth hour, it means the shop is closed at the hour j.

Example 1:
Input: customers = "YYNY"
Output: 2
Explanation:
- Closing the shop at the 0th hour incurs in 1+1+0+1 = 3 penalty.
- Closing the shop at the 1st hour incurs in 0+1+0+1 = 2 penalty.
- Closing the shop at the 2nd hour incurs in 0+0+0+1 = 1 penalty.
- Closing the shop at the 3rd hour incurs in 0+0+1+1 = 2 penalty.
- Closing the shop at the 4th hour incurs in 0+0+1+0 = 1 penalty.
Closing the shop at 2nd or 4th hour gives a minimum penalty. Since 2 is earlier, the optimal closing time is 2.

Example 2:
Input: customers = "NNNNN"
Output: 0
Explanation: It is best to close the shop at the 0th hour as no customers arrive.

Example 3:
Input: customers = "YYYY"
Output: 4
Explanation: It is best to close the shop at the 4th hour as customers arrive at each hour.
"""


class Solution:
    def bestClosingTime(self, customers: str) -> int:

        # Intuition:
        # By understanding the question, we can come up with the Brute Force Solution: At any index, the penalty is the sum of prefix count of ‘N’ and suffix count of ‘Y’. Traverse from 0 to len(customers) + 1, break customers into customers[:i] and customers[i:], calculate the "N" and "Y" to get penalty. This method leads to O(N^2) tc.
        # By observing the examples, we find that, by firstly calculate the penalty of not opening at all, we can form this question into a prefix sum problem:
        # Traverse thorugh visit in customers, if "Y", the penalty -= 1, else, penalty += 1. This method leads to O(N) tc.

        penalty = 0
        ans = 0
        for visit in customers:  # don't open at all
            if visit == "Y":
                penalty += 1
        min_penalty = penalty
        for i in range(len(customers)):
            if customers[i] == "Y":
                penalty -= 1
            else:
                penalty += 1
            if penalty < min_penalty:
                min_penalty = penalty
                ans = i + 1
        return ans
