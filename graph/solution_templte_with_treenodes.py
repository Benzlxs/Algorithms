
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



class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        self.nexts = []

root_node = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)
node_4 = TreeNode(4)
node_5 = TreeNode(5)
node_6 = TreeNode(6)
node_7 = TreeNode(7)
node_8 = TreeNode(8)
node_9 = TreeNode(9)
node_10 = TreeNode(10)

def littleTree(root,left,right):
    root.left = left
    root.right = right
    if root.left:
        root.nexts.append(root.left)
    if root.right:
        root.nexts.append(root.right)

littleTree(root_node, node_2, node_3)
littleTree(node_2, node_4, node_5)
littleTree(node_3, node_6, node_7)
littleTree(node_4, node_8, node_9)
littleTree(node_5, node_10, None)


func=Solution()
results = func.KthNode(root_node, 3)
print(results)
