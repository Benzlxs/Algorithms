"""
Problem
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

"""


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self.dfs(1, n+1)

    def dfs(self, start, end):
        if start == end:
            return None
        result = []
        for i in range(start, end):
            for l in self.dfs(start, i) or [None]:
                for r in self.dfs(i+1, end) or [None]:
                    node = TreeNode(i)
                    node.left, node.right  = l, r
                    result.append(node)
        return result

