"""
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:

        # Intuition:
        # if we know the substring within i,j is a palindrome, and s[i-1] == s[j+1], then i-1,j+1 is also palindrome
        # we know substrings of length 1 is paalindrome, so we can check those of length 3
        # for even-length palindrom, we know if s[i] == s[i+1], then i,i+1 is palidrome
        # this forms a DP problem

        # define the state variables
        ans = [0, 0]

        # define the dp array
        dp = [[False for i in range(len(s))] for i in range(len(s))]

        # define the initial values
        for i in range(len(s)):
            dp[i][i] = True
        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                ans = [i, i + 1]

        # define the state transition functions
        for diff in range(2, len(s)):  # diff: substrings of all length from small to big
            for i in range(0, len(s) - diff):  # i: start point of the substring
                j = i + diff  # j: end point of the substring
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    ans = [i, j]

        return s[ans[0]: ans[1] + 1]

