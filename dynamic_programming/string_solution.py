## using dynamic programming to solve the minmum time of crossing bridge
'''
Logic:
    1. sort the times
    2. the first two persons cross the bridege first;
    3. if only one people doesn't cross the bright, the first guy cross the bridge, and bring the one back;
    4. if two persons doesn't cross, there are two solutions: one is to repeat 3 twices, two is that the first guy cross back (with torch), then two other person cross bright, the second fastest guy crosses back with torch to bring the fastest guys back;
'''


import os
import fire
import time
import numpy as np
import time




class Solution1:
    def __init__(self):
        self.all_combination = []

    def num_str(self, strings ):
        # write code here
        if not strings:
            return strings

        string_b = [i for i in reversed(strings)]
        string_len = len(strings)+1
        lsc = []
        for i in range(string_len):
            lsc.append([0]*string_len)

        for i in range(1,string_len):
            for j in range(1,string_len):
                if strings[i-1] == string_b[j-1]:
                    lsc[i][j] = lsc[i-1][j-1] +1
                else:
                    lsc[i][j] = max(lsc[i][j-1], lsc[i-1][j])
        return len(strings) - lsc[string_len-1][string_len-1]



class Solution2:
    def __init__(self):
        self.all_combination = []
        self.s = 0

    def dp(self, i, j):
        if i>=j:
            return 0
        if self.s[i]==self.s[j]:
            return self.dp(i+1, j -1)
        return min(self.dp(i+1,j), self.dp(i,j-1)) + 1

    def num_str(self, strings ):
        # write code here
        if not strings:
            return strings
        self.s = strings
        string_len = len(strings)

        return self.dp(0, string_len-1)






if __name__=='__main__':
    strings = 'abcde'
    t1 = time.time()
    #rs = jumpfloor(n)
    test = Solution2()
    result = test.num_str(strings)
    #rs = numberof1(-4)
    print("Time: {}, Results: {}".format(time.time()-t1, result))

