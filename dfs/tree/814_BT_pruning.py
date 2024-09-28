"""
Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

A subtree of a node node is node plus every node that is a descendant of node.
"""

"""
Intuition

Prune children of the tree recursively => DFS
The only decisions at each node are whether to prune the left child or the right child.

Define a function that 
    1. tells us whether the subtree at this node contains a 1 
    2. prunes all subtrees that do not contain 1 (via node.left = null)
"""


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def contains_one(node: TreeNode) -> bool:
            if not node:
                return False
            # check left subtree
            left_contains_one = contains_one(node.left)
            # check right subtree
            right_contains_one = contains_one(node.right)

            if not left_contains_one:
                node.left = None

            if not right_contains_one:
                node.right = None

            # return True if the current node is 1 or left/right subtrees contains a 1
            return node.val or left_contains_one or right_contains_one

        # return the pruned tree if the tree contains a 1, otherwise return None
        return root if contains_one(root) else None
