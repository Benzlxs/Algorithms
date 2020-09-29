

def bfs_1(node):
    if node is None:
        return
    queue = []
    #nodeSet = set()
    queue.insert(0,node)
    #nodeSet.add(node)
    while queue:
        cur = queue.pop()               # 弹出元素
        print(cur.val)                # 打印元素值
        for next in cur.nexts:          # 遍历元素的邻接节点
            #if next not in nodeSet:     # 若邻接节点没有入过队，加入队列并登记
                #nodeSet.add(next)
                queue.insert(0,next)


def bfs_0(node):
    if node is None:
        return
    queue = []
    #nodeSet = set()
    queue.insert(0,node)
    #nodeSet.add(node)
    while queue:
        next_level = []
        for cur in queue:
            print(cur.val)
            if cur.left:
                next_level.append(cur.left)
            if cur.right:
                next_level.append(cur.right)
        queue = next_level



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

bfs_0(root_node)
print('One more')
bfs_1(root_node)
