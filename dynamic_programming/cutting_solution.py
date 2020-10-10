"""

"""


import os
import fire
import time
import numpy as np
import time




class Solution:
    def __init__(self):
        self.all_combination = []

    def cutting(self, lens, prices):
        # write code here
        if lens == 0:
            return 0
        local_optimal = [0, 0]
        for i in range(1,lens+1):
            q = -1
            for j in range(1,min(len(prices)+1,i+1)):
                # iteration between optimal substructure
                q = max(q, prices[j-1]+local_optimal[i-j+1])
            local_optimal.append(q)
        return local_optimal[-1]






if __name__=='__main__':
    steel_lens = 13
    prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    t1 = time.time()
    #rs = jumpfloor(n)
    test = Solution()
    result = test.cutting(steel_lens, prices)
    #rs = numberof1(-4)
    print("Time: {}, Results: {}".format(time.time()-t1, result))

