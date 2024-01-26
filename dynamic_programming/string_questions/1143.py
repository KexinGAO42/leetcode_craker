"""
Given two strings text1 and text2, return the length of their longest common subsequence.
If there is no common subsequence, return 0.
A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # S1: define state variable

        # S2: define dp structure

        dp = [[0 for i in range(len(text1) + 1)] for i in range(len(text2) + 1)]
        """
            - a b c d e
        -
        a     1 1 1 1 1
        c     1 1 2 2 2
        e     1 1 2 2 3

            b l
        y   0 0
        b   1 1
        y   1 1
        """

        # S3: initialize dp

        # S4: define trnasition function
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if text2[i - 1] == text1[j - 1]:  # if c == b
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]
