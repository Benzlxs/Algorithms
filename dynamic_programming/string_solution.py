## using dynamic programming to solve the minmum time of crossing bridge
'''
Logic:
    1. sort the times
    2. the first two persons cross the bridege first;
    3. if only one people doesn't cross the bright, the first guy cross the bridge, and bring the one back;
    4. if two persons doesn't cross, there are two solutions: one is to repeat 3 twices, two is that the first guy cross back (with torch), then two other person cross bright, the second fastest guy crosses back with torch to bring the fastest guys back;

题目：所谓回文字符串，就是一个字符串，从左到右读和从右到左读是完全一样的，比如"aba"。当然，
    我们给你的问题不会再简单到判断一个字符串是不是回文字符串。现在要求你，
    给你一个字符串，可在任意位置添加字符，最少再添加几个字符，可以使这个字符串成为回文字符串。

    解题思路：
    典型的区间模型，回文串拥有很明显的子结构特征，即当字符串X是一个回文串时，在X两边各添加一个字符‘a’后，aXa仍然是一个回文串，
    我们用d[i][j]来表示A[i…j]这个子串变成回文串所需要添加的最少的字符数，
    那么对于A[i] == A[j]的情况，很明显有 d[i][j] = d[i+1][j-1] （这里需要明确一点，
    当i+1 > j-1时也是有意义的，它代表的是空串，空串也是一个回文串，所以这种情况下d[i+1][j-1] = 0）；
    当A[i] != A[j]时，我们将它变成更小的子问题求解，我们有两种决策

'''


import os
import fire
import time
import numpy as np
import time



# dynamic programming
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
                    # get value from diagnal
                    lsc[i][j] = lsc[i-1][j-1] +1
                else:
                    # get value from sides
                    lsc[i][j] = max(lsc[i][j-1], lsc[i-1][j])
        return len(strings) - lsc[string_len-1][string_len-1]


## recursive
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

