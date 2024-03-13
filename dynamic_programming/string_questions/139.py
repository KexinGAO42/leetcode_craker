"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # Intuition: create a 1D DP of len(s) + 1 to store T/F.
        # Initialzation:
        #   dp[0] = True
        # General case should meet two criteria:
        #   1. one segmentation in dp is True
        #   2. another segmentation in words
        # e.g "leetcod*e*"
        #   if dp[l] and "eetcode" in words
        #   if dp[le] and "etcode" in words
        # ...if dp[leet] and "code" in words => Yes! => dp[leetcode] is True
        # return dp[-1]

        words = set(wordDict)

        # S1: create dp
        dp = [False for i in range(len(s) + 1)]

        # S2: initialize dp
        dp[0] = True

        # S3: define state transition functions
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j: i] in words:
                    dp[i] = True
                    break

        return dp[-1]

