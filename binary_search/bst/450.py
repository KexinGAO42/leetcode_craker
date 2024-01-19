"""
Given a root node reference of a BST and a key, delete the node with the given key in the BST.
Return the root node reference (possibly updated) of the BST.
Basically, the deletion can be divided into two stages:
1. Search for a node to remove.
2. If the node is found, delete the node.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return root

        # S1: binary seaarch the tree until find the key
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:  # we find the key
            # if the key node only has right child, replace the node with right child
            if not root.left:
                root = root.right
            # same thing for only having left child
            elif not root.right:
                root = root.left
            else:  # IMPORTANT: if the key node has two child
                # find the min from right subtree (keep traversing to left)
                cur = root.right
                while cur.left:
                    cur = cur.left
                root.val = cur.val
                # recursively delete the right child
                root.right = self.deleteNode(root.right, root.val)

        return root
