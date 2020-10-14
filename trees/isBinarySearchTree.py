"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

"""


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root, float('-inf'), float('inf'))

    def helper(self, root, low, high):

        if not root:
            return True

        value = root.val

        if (value > low and value < high) and  self.helper(root.left, low, root.val) and self.helper(root.right, root.val, high):
            return True
        else:
            return False
