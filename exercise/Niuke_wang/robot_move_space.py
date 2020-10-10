'''
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
但是不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？

'''

import time

class Solution:
    def __init__(self):
        self.mark = []
        self.threshold=None
        self.rows = None
        self.cols = None
        self.dirs = [-1, 0, 1, 0, -1]
        self.count = 0
    def check(self, n):
        sum = 0
        while n:
            sum+= n%10
            n /= 10
        return sum
    def move_rob(self, u, v):
        if u < 0 or v<0 or u>= self.rows or v>= self.cols or self.mark[u][v]==1:
            return
        if (self.check(u) + self.check(v)) > self.threshold:
            return
        self.mark[u][v] = 1
        self.count += 1
        for i in range(4):
            self.move_rob(u+self.dirs[i], v+self.dirs[i+1])
    def movingCount(self, threshold, rows, cols):
        # write code here
        for i in range(rows):
            self.mark.append([0 for j in range(cols)])
        self.rows = rows
        self.cols = cols
        self.threshold = threshold
        self.move_rob(0,0)
        # return sum([sum(vec) for vec in self.mark])
        return self.count




if __name__=='__main__':
    inputs = 'ab*ac*a'
    number = 13
    s='aaa'
    t1 = time.time()
    #rs = jumpfloor(n)
    test = Solution()
    result = test.movingCount(15, 20, 20)
    #rs = numberof1(-4)
    print("Time: {}, Results: {}".format(time.time()-t1, result))

