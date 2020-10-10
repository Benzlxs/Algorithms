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

    def recursive(self, s, dic, coms):
        if s.count('_') == len(s):
            # end state of recursives
            self.all_combination.append(coms)  # if find a solution
        dic_len  = len(dic)
        for i in range(dic_len):
            num_count = s.count(dic[i])
            if num_count > 0: # no word in dictionary, just skip
                for j in range(num_count):
                    str_start = s.index(dic[i])
                    first_half = s[:str_start]
                    str_end = str_start + len(dic[i])
                    second_half = s[str_end:]
                    # re-divide
                    rest_string = first_half + '_' + second_half
                    # using the tmep_com to trace all already-split words for
                    # the end state solutions
                    temp_com = coms + [dic[i]]
                    self.recursive(rest_string, dic[i:], temp_com)

    def run(self, s, dic):
        order_dict  = []  # ordered
        len_words = [len(i) for i in dic]
        #  re-order the dictionary from longest to shortest
        while (len_words != []):
            len_max = max(len_words)
            idx_max = len_words.index(len_max)
            order_dict.append(dic.pop(idx_max))
            len_words.pop(idx_max)
        self.recursive(s, order_dict, [])




if __name__=='__main__':
    inputs ='ilikealibaba'
    number = 13
    dic = ['i', 'like', 'ali', 'liba', 'baba', 'alibaba']
    t1 = time.time()
    test = Solution()
    result = test.run(inputs, dic)
    print("Time: {}, Results: {}".format(time.time()-t1, test.all_combination))

