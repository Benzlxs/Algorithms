'''
请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。
在本题中，匹配是指字符串的所有字符匹配整个模式。
例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配

'''

import time

class Solution:
    def match(self, s, pattern):
        # write code here
        if len(s) == 0 and len(pattern) == 0:
            return True
        if len(s) > 0 and len(pattern) == 0:
            return False
        # 如果模式第二个字符是*
        if len(pattern) > 1 and pattern[1] == '*':
            if len(s) > 0 and (s[0] == pattern[0] or pattern[0] == '.'):
                # 如果第一个字符匹配，三种可能1、字符串移1位；2、字符串移1位，模式移2位；3、模式后移两位(这里将2、3合并书写)
                return self.match(s, pattern[2:]) or self.match(s[1:], pattern)  # 递归入口
            else:
                # 如果第一个字符不匹配，模式往后移2位，相当于忽略x*
                return self.match(s, pattern[2:])    # 递归入口
        # 如果模式第二个字符不是*
        if len(s) > 0 and (s[0] == pattern[0] or pattern[0] == '.'):
            return self.match(s[1:], pattern[1:])   # 递归入口
        else:
            return False

class Solution2:
    def match(self, s, pattern):
        # write code here
        ns = len(s)
        np = len(pattern)
        if ns == 0 or np == 0:
            return False
        # initialization
        f = []
        for i in range(ns):
            f.append([0 for j in range(np)])
        f[0][0] = 1
        # dynamic programming
        for i in range(ns):
            for j in range(1, np):
                if pattern[j-1] != '*':
                    if i>=1 and (s[i-1]==pattern[j-1] or pattern[j-1]=='.'):
                        f[i][j] = f[i-1][j-1]
                else:
                    if j>=2:
                        f[i][j] =  f[i][j] or f[i][j-2]
                    if (i>=1 and j>=2 and ( s[i-1]==pattern[j-2] or pattern[j-2]=='.' )):
                        f[i][j] = f[i-1][j]
        return f[-1][-1]


if __name__=='__main__':
    inputs = 'ab*ac*a'
    number = 13
    s='aaa'
    t1 = time.time()
    #rs = jumpfloor(n)
    test = Solution()
    result = test.match(s, inputs)
    #rs = numberof1(-4)
    print("Time: {}, Results: {}".format(time.time()-t1, result))

