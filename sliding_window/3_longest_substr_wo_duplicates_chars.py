"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

"""
Intuition:
1. Use two pointers: start and end to form a sliding window.
2. Use a set to track characters in the current window.
3. Expand the window by moving end until a duplicate is found.
4. If a duplicate is found, move start to shrink the window until the duplicate is removed.
5. Keep track of the maximum window size with unique characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window + set (less space more time)
        # corner case
        if not s:
            return 0
        if len(s) == 1:
            return 1
        # general
        dup = set(s[0])
        l = 0
        res = 0
        for i in range(1, len(s)):
            if s[i] in dup:
                while s[i] in dup:
                    print(dup, s[l], s[i])
                    dup.remove(s[l])
                    l += 1
            dup.add(s[i])
            res = max(res, i - l + 1)
        return res

        # Sliding window optimized (less time more space)
        if not s:
            return 0
        if len(s) == 1:
            return 1
        res = 0
        l = 0
        index = {s[0]: 0}
        for i in range(1, len(s)): # i => right pointer
            if s[i] in index.keys() and index[s[i]] >= l: # when we encounter duplicated char, and the l pointer is on the left of the index of the duplicaated char
                l = index[s[i]] + 1
            index[s[i]] = i
            res = max(res, i - l + 1)
        return res

