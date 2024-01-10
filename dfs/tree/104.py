"""
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # intuition: traverse the tree from root, when reach a leaf, record the depth

        # Base Case 1: when a node is not in the tree
        def dfs(node, depth):
            if not node:
                return depth
            return max(dfs(node.left, depth + 1), dfs(node.right, depth + 1))

        return dfs(root, 0)

        # Base Case 2: when aa node is leaf
        if not root:
            return 0

        def dfs(node, depth):
            if not node.left and not node.right:
                return depth

            res = depth
            if node.left:
                left_depth = dfs(node.left, depth + 1)
                res = max(res, left_depth)

            if node.right:
                right_depth = dfs(node.right, depth + 1)
                res = max(res, right_depth)

            return res

        return dfs(root, 1)
