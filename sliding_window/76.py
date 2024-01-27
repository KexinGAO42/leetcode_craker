"""
Given two strings s and t of lengths m and n respectively, return the minimum window
substring of s such that every character in t (including duplicates) is included in the window.
If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
"""


from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # Intuition: we want to find a substring of s that covers all characters in t;
        # also, we want the length of the substring to be minimized
        # this seems to be a sliding window problems realized by two pointers

        # when to move the slow pointer?
        # when the s[slow:fast] covers all characters in t, we move the s

        slow, fast = 0, 0
        t_map = defaultdict(int)
        window = defaultdict(int)
        sub_len = inf
        ans = None

        for c in t:
            t_map[c] += 1

        target = len(t_map)
        match = 0

        while fast < len(s):
            window[s[fast]] += 1
            if s[fast] in t_map and window[s[fast]] == t_map[s[fast]]:
                match += 1
            fast += 1
            while match == target and slow < fast:
                if fast - slow < sub_len:
                    ans = s[slow : fast]
                    sub_len = fast - slow
                window[s[slow]] -= 1
                if s[slow] in t_map and window[s[slow]] < t_map[s[slow]]:
                    match -= 1
                slow += 1

        if sub_len == inf:
            return ""

        return ans
