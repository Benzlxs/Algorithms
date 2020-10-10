## using dynamic programming to solve the minmum time of crossing bridge
## explaination: https://zhuanlan.zhihu.com/p/68228645
"""
有[公式]件物品和一个容量为[公式]的背包。第[公式]件物品的体积是[公式]，其价值是[公式]。
求解，在不超过背包容量情况下，将哪些物品装入背包可使价值总和最大。


用子问题定义状态：即 [公式] 表示前 [公式] 件物品恰放入一个容量为 [公式] 的背包可以获得的最大价值。则其状态转移方程便是：
"""

import os
import fire
import time
import numpy as np
import time




class Solution:
    def __init__(self):
        self.all_combination = []

    def package(self, weight, value, v):
        if len(weight)==0  or (v<0):
            return 0
        obj_len = len(weight)
        # initializing
        sub_opt = []
        for i in range(obj_len+1):
            sub_opt.append([0]*v)

        for i in range(1, (obj_len+1)):
            for j in range(1, v):
                if weight[i-1] <= j:
                    sub_opt[i][j] = max(sub_opt[i-1][j],
                                        sub_opt[i-1][j-weight[i-1]]+value[i-1] )
                else:
                    sub_opt[i][j] = sub_opt[i-1][j]
        return sub_opt[-1][-1]






if __name__=='__main__':
    v = 10
    weight  = [5,6,5,1,19,7]
    value = [2,3,1,4,6,5]
    # times = [1, 2, 5, 10]
    t1 = time.time()
    #rs = jumpfloor(n)
    test = Solution()
    result = test.package(weight, value, v)
    #rs = numberof1(-4)
    print("Time: {}, Results: {}".format(time.time()-t1, result))

