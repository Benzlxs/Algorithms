#树的深度优先搜索
# 用递归的方法进行dfs
#nodeSet = set()
def dfs1(node):
    if node is None:
        return
    #nodeSet.add(node)
    print(node.val)
    #相当于树的前序遍历了，只不过这里把左右子节点放到了nexts的列表中
    for next in node.nexts:
        #if next not in nodeSet:
            dfs1(next)


# 用循环的方法进行dfs
def dfs(node):
    if node is None:
        return
    nodeSet = set()
    stack = []
    print(node.val)
    nodeSet.add(node)
    stack.append(node)
    while len(stack) > 0:
        cur = stack.pop()               # 弹出最近入栈的节点
        for next in cur.nexts:         # 遍历该节点的邻接节点
            if next not in nodeSet:    # 如果邻接节点不重复
                stack.append(cur)       # 把节点压入
                stack.append(next)      # 把邻接节点压入
                nodeSet.add(next)           # 登记节点
                print(next.val)       # 打印节点值
                break                   # 退出，保持深度优先


#实现一个二叉树，并且用BFS或DFS去遍历她
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

dfs(root_node)
dfs1(root_node)
