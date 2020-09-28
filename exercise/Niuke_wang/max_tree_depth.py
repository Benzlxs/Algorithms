'''
Question:
输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。

'''
import os
import fire
import time
import numpy as np
import time


## recursive
class Solution:
    def TreeDepth(self, pRoot):
        if pRoot is None:
            return 0

        depth_left = self.TreeDepth(pRoot.left)
        depth_right = self.TreeDepth(pRoot.right)

        return 1 + (depth_left if depth_left > depth_right else depth_right)


## iteration
class Solution:
    def TreeDepth(self, pRoot):
        if pRoot is None:
            return 0

        next_nodes = []
        next_nodes.append(pRoot)
        depth = 0
        while next_nodes:
            num_nodes = len(next_nodes)
            temp_nodes = []
            for i in range(num_nodes):
                cur_node = next_nodes[i]
                if cur_node.left:
                    temp_nodes.append(cur_node.left)
                if cur_node.right:
                    temp_nodes.append(cur_node.right)

            depth += 1
            next_nodes = temp_nodes

        return depth




if __name__=='__main__':
    inputs = [1,2,3,4,5,6,7,0]
    number = 13
    s='googgle'
    t1 = time.time()
    listA = [0,9,1,2,4]
    listB = [3,2,4]
    #rs = jumpfloor(n)
    test = Solution()
    result = test.FindFirstCommonNode(listA, listB)
    #rs = numberof1(-4)
    print("Time: {}, Results: {}".format(time.time()-t1, result))

