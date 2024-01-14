"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
You have the following three operations permitted on a word:
Insert a character
Delete a character
Replace a character

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Intuition: Levenstein Distance
        We form a matrix(dp) wheren num_col = len(word1) + 1, num_row = len(word2) + 1
            ' ' 'h' 'o' 'r' 's' 'e'
        ' ' 0    1   2   3   4   5
        'r' 1
        'o' 2
        's' 3
        Each cell (dp[i][j]) indicates to modify word1[j] to word2[i], the mininum number of operations
        We intialize the dp with empty string at the beginning of each word
        Based on the initialization, we calculate the min_num of operations:
            - deletion: dp[i-1][j] + 1
            - insertion: dp[i][j-1] + 1
            - substitution: dp[i-1][j-1] + substition_cost
        if the two chars are same: substition_cost = 0
        else: substition_cost = 1
        dp[i][j] = min(dp[i-1][j-1] + substition_cost, dp[i][j-1] + 1, dp[i-1][j] + 1)
        return the right bottom cell as the min_num of operations to modify the whole string
        """

        # S1: define variables
        c, r = len(word1), len(word2)

        # S2: build the dp structure
        dp =[[0 for i in range(c + 1)] for j in range(r + 1)]

        # S3: initialize values
        for i in range(1, c + 1):
            dp[0][i] = i
        for i in range(1, r + 1):
            dp[i][0] = i

        # S4: define transition functions
        for i in range(1, r + 1):
            for j in range(1, c + 1):
                if word2[i - 1] == word1[j - 1]:
                    sub_cost = 0
                else:
                    sub_cost = 1
                dp[i][j] = min(dp[i - 1][j - 1] + sub_cost, dp[i][j - 1] + 1, dp[i - 1][j] + 1)
        return dp[r][c]