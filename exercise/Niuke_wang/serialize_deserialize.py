"""
请实现两个函数，分别用来序列化和反序列化二叉树

二叉树的序列化是指：把一棵二叉树按照某种遍历方式的结果以某种格式保存为字符串，从而使得内存中建立起来的二叉树可以持久保存。
序列化可以基于先序、中序、后序、层序的二叉树遍历方式来进行修改，序列化的结果是一个字符串，
序列化时通过 某种符号表示空节点（#），以 ！ 表示一个结点值的结束（value!）。

"""


class Solution:
    def Serialize(self, root):
        valuelist = []
        self.preorder(root, valuelist)
        # 将结点值序列转化为一个字符串
        return ','.join(map(str, valuelist))
    def preorder(self, root, valuelist):
        if not root:
            # 对于空结点，返回#字符加以标识
            valuelist.append('#')
            return None
        valuelist.append(root.val)
        self.preorder(root.left, valuelist)
        self.preorder(root.right, valuelist)
    # write code here
    def Deserialize(self, s):
        valuelist = s.split(',')
        root = self.preorderdes(valuelist)
        return root
    def preorderdes(self, valuelist):
        if len(valuelist) == 0 or valuelist[0] == '':
            return None
        # 遇到#字符，直接删除，返回空结点
        if valuelist[0] == '#':
            del valuelist[0]
            return None
        root = TreeNode(int(valuelist[0]))
        del valuelist[0]
        root.left = self.preorderdes(valuelist)
        root.right = self.preorderdes(valuelist)
        return root
