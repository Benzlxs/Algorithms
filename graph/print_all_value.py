"""
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
"""



class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        # 当前层
        current = [pRoot]
        # 当前层子节点
        next_layer = []
        # 结果值
        result = []
        # 用于判断正序或者逆序输出
        count = 1
        while current:
            # 把当前层的子节点都添加到下一层
            for i in current:
                if i.left:
                    next_layer.append(i.left)
                if i.right:
                    next_layer.append(i.right)
            # 如果取余2存在，则正序打印，反之亦然
            if count%2:
                count+=1
                result.append([i.val for i in current])
            else:
                count += 1
                result.append([i.val for i in current[::-1]])
            #把下一层换成当前层
            current,next_layer = next_layer,[]
        return result

