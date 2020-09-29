"""

给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。
"""


class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        self.res=[]
        self.mid(pRoot)
        return self.res[k-1] if 0<k<=len(self.res) else None
    def mid(self,root):
        if not root:
            return None
        self.mid(root.left)
        self.res.append(root)
        self.mid(root.right)
