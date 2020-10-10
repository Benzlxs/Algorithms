"""
Construct Binary Tree from Inorder and Postorder Traversal
"""



class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if (inorder == []) or (postorder == []):
            return None
        root = TreeNode(postorder.pop())
        ind = inorder.index(root.val)
        root.right = self.buildTree(inorder[ind+1:], postorder[ind:])
        root.left = self.buildTree(inorder[:ind], postorder[:ind])
        return root
