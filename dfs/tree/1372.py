"""
You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:

Choose any node in the binary tree and a direction (right or left).
If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
Change the direction from right to left or from left to right.
Repeat the second and third steps until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        # The current path length is maintained in two variables - left and right.
        # At each node, if we go left, we update left by adding 1 to right and reset right to 0.
        # Conversely, if we go right, we add 1 to left and reset left to 0.
        # This way, we always start a new path with either (0,1) or (1,0).

        # S1: define variables
        self.max_len = 0

        # S3: define dfs
        def dfs(node, left, right):
            # define base case
            if not node.left and not node.right:
                self.max_len = max(self.max_len, left, right)
                return
            # process current node
            self.max_len = max(self.max_len, left, right)
            # process neighbors
            if node.left:
                dfs(node.left, 1 + right, 0)
            if node.right:
                dfs(node.right, 0, 1 + left)

        # S2: define main function
        dfs(root, 0, 0)
        return self.max_len
