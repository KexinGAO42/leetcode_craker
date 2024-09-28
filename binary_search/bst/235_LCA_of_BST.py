"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
"""

"""
# 3 traits of BST:
# 1. Both root's subtrees also are binary;
# 2. All LEFT child nodes of LEFT subtree have values less or equal the value of the current node.
# 3. All RIGHT child nodes of RIGHT subtree have values greater the value of the current node.

# According to the traits above
# If current node value > p.value and q.value:
#   right subtree will be even greater, so go left
# If current node value < p.value and q.value:
#   left subtree will be even greater, so go right
# If not both => LCA found
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Iterative solution
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_val, q_val = p.val, q.val
        cur_node = root

        while cur_node:
            if p_val > cur_node.val and q_val > cur_node.val:
                cur_node = cur_node.right
            elif p_val < cur_node.val and q_val < cur_node.val:
                cur_node = cur_node.left
            else:
                return cur_node


# Recursive solution
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent_val, p_val, q_val = root.val, p.val, q.val
        if p_val > parent_val and q_val > parent_val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p_val < parent_val and q_val < parent_val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root
