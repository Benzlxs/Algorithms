"""
Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.
"""


class Solution:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if (root is None):
            return ""

        # preorder traversal
        stack = [root]
        output = []

        while (stack):
            node = stack.pop()
            output.append(node.val)

            if (node.right):
                stack.append(node.right)
            if (node.left):
                stack.append(node.left)

        return " ".join([str(val) for val in output])


    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if (data == ""):
            return None

        vals = [int(val) for val in data.split()]
        counter = 0

        def buildTree(minVal, maxVal):
            nonlocal counter
            if counter >= len(vals):
                return None
            if (vals[counter] < minVal or vals[counter] > maxVal):
                return None


            node = TreeNode(vals[counter])
            counter += 1
            node.left = buildTree(minVal, node.val)
            node.right = buildTree(node.val, maxVal)

            return node

        return buildTree(float("-inf"), float("inf"))


