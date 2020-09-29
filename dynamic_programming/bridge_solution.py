## using dynamic programming to solve the minmum time of crossing bridge
'''

题目：在一个夜黑风高的晚上，有n（n <= 50）个小朋友在桥的这边，现在他们需要过桥，但是由于桥很窄，每次只允许不大于两人通过，
    他们只有一个手电筒，所以每次过桥的两个人需要把手电筒带回来，i号小朋友过桥的时间为T[i]，
    两个人过桥的总时间为二者中时间长者。问所有小朋友过桥的总时间最短是多少。


    我们先将所有人按花费时间递增进行排序，假设前i个人过河花费的最少时间为opt[i]，那么考虑前i-1个人过河的情况，即河这边还有1个人，河那边有i-1个人，并且这时候手电筒肯定在对岸，所以opt[i] = opt[i-1] + a[1] + a[i](让花费时间最少的人把手电筒送过来，然后和第i个人一起过河)

    如果河这边还有两个人，一个是第i号，另外一个无所谓，河那边有i-2个人，并且手电筒肯定在对岸，所以opt[i] = opt[i-2] + a[1] + a[i] + 2*a[2] (让花费时间最少的人把电筒送过来，然后第i个人和另外一个人一起过河，由于花费时间最少的人在这边，所以下一次送手电筒过来的一定是花费次少的，送过来后花费最少的和花费次少的一起过河，解决问题)

    所以 opt[i] = min{opt[i-1] + a[1] + a[i] , opt[i-2] + a[1] + a[i] + 2*a[2] }。

    来看一组数据，四个人过桥花费的时间分别为：1 2 5 10

    具体步骤是这样的：

    第一步：1和2过去，花费时间2，然后1回来（花费时间1）；

    第二歩：3和4过去，花费时间10，然后2回来（花费时间2）；

    第三部：1和2过去，花费时间2，总耗时17。

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

