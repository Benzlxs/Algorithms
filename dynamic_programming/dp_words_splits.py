"""
Question:
    spliting the string with the wrods in dictionary
"""


import os
import fire
import time
import numpy as np
import time



class Solution:
    def __init__(self):
        self.all_combination = []


    def run(self, s, dic):
        order_dict  = []  # ordered
        if s in dic:
            return s

        # sub-groups of words
        sub_sample = [[i] for i in dic]

        for i in range(1, len(s)):
            if s[:i] not in dic:
                for j in range(1,i):
                    if s[:j] in dic and s[j:i] in dic:
                        dic.append(s[:i])
                        idx_1 = dic.index(s[:j])
                        idx_2 = dic.index(s[j:i])
                        sub_sample.append(sub_sample[idx_1] + sub_sample[idx_2])
        results = []
        i = len(s)
        if s[:i] not in dic:
            for j in range(1,i):
                if s[:j] in dic and s[j:] in dic:
                    dic.append(s[:i])
                    idx_1 = dic.index(s[:j])
                    idx_2 = dic.index(s[j:i])
                    results.append(sub_sample[idx_1] + sub_sample[idx_2])
        return results




if __name__=='__main__':
    inputs ='ilikealibaba'
    number = 13
    dic = ['i', 'like', 'ali', 'liba', 'baba', 'alibaba']
    t1 = time.time()
    test = Solution()
    result = test.run(inputs, dic)
    print("Time: {}, Results: {}".format(time.time()-t1, result))

