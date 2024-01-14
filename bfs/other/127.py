"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

Example 1:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

Example 2:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
"""

from collections import defaultdict, deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        """
        Intuition: we want to find the shortest sequence, so we use BFS
        Only one letter can be changed at a time, for example:
                hit
            *it h*t hi*
            ... ... ...
        In order to continue searching, we need to know the children of *it, h*t, hi*, by looking up the dict
        To do this, we need to build a change map: *ot: hot, dot, lot
        """

        # S1: create the map
        l = len(beginWord)
        change_map = defaultdict(list)
        for word in wordList:
            for i in range(l):
                key = word[:i] + "*" + word[i + 1:]
                change_map[key].append(word)

        # S2: define BFS
        # Initialize queue for BFS
        queue = deque([(beginWord, 1)])  # (word, count)
        # Mark the start word as visited
        visited = set(beginWord)
        # while loop
        while queue:
            crt, lvl = queue.popleft()
            # process current word
            for i in range(len(crt)):
                key = crt[:i] + "*" + crt[i + 1:]
                # process neighbors
                for val in change_map[key]:
                    if val == endWord:
                        return lvl + 1
                    if val not in visited:
                        visited.add(val)
                        queue.append((val, lvl + 1))
        # If we cannot find any path, return 0
        return 0
