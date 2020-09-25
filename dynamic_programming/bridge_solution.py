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




class Solution:
    def __init__(self):
        self.all_combination = []

    def crossing(self, num, times ):
        # write code here
        if num <= 0:
            return 0
        if num<=2:
            return sum(times)
        if num ==3:
            return times[0]+times[1]+times[2]
        times.sort() # sortting the time
        suboptimal = []
        suboptimal.append(times[0]) # cross alone
        suboptimal.append(times[1]) # cross together
        suboptimal.append(times[0]+times[1]+times[2])
        for i in range(3,num):
            min_time = min(suboptimal[i-1]+times[0]+times[i],
                           suboptimal[i-2]+times[i]+2*times[1]+times[0])
            suboptimal.append(min_time)
        return suboptimal[-1]




if __name__=='__main__':
    num_kids = 4
    times = [1, 2, 5, 10]
    t1 = time.time()
    #rs = jumpfloor(n)
    test = Solution()
    result = test.crossing(num_kids, times)
    #rs = numberof1(-4)
    print("Time: {}, Results: {}".format(time.time()-t1, result))

