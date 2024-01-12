"""
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

Example 1:
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.

Example 2:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        # Intuition: traverse the tree recursively (DFS)
        # at each node, we store all sum from previous nodes (e.g. 10 - 5 - 3 - 2 - 1, at node 2, we store [20, 10, 5, 2])
        # at each node, we add the node val and each sum in the list, check whether it's equal to targetSum

        if not root:
            return 0

        # S1: define variables
        self.res = 0
        memo = defaultdict(list)

        # S3: define dfs
        def dfs(node, prev_node):
            # define base case
            if not node.left and not node.right:
                if node.val == targetSum:
                    self.res += 1
                if prev_node:
                    for sum_val in memo[prev_node]:
                        memo[node].append(sum_val + node.val)
                        if sum_val + node.val == targetSum:
                            self.res += 1
                    memo[node].append(node.val)
                return
            # process current node
            if node.val == targetSum:
                    self.res += 1
            if prev_node:
                for sum_val in memo[prev_node]:
                    memo[node].append(sum_val + node.val)
                    if sum_val + node.val == targetSum:
                        self.res += 1
                memo[node].append(node.val)
            # process neighbors
            if node.left:
                dfs(node.left, node)
            if node.right:
                dfs(node.right, node)

        # S2: define main function
        memo[root].append(root.val)
        dfs(root, None)
        return self.res
