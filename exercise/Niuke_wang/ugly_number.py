"""
Question:
    The number which can be divide by 2,3, and 5, is called Ugly Number, For example, 8 is, whle 14 isn't. 1 is also treated as a urgly number.
    Print the N_th urgly ugly number
"""


import time


class solution:
    def run(self, n):
        if n == 0:
            return 0
        ugly_list = [1]
        p2 = 0
        p3 = 0
        p5 = 0
        for i in range(1, n):
            new_ugly = min(ugly_list[p2]*2, ugly_list[p3]*3, ugly_list[p5]*5)
            if new_ugly%2 == 0:
                p2 += 1
            if new_ugly%3 == 0:
                p3 += 1
            if new_ugly%5 == 0:
                p5 += 1
            ugly_list.append(new_ugly)
        return ugly_list[-1]




if __name__ == '__main__':

    n = 10
    test = solution()
    result = test.run(n)

    print('results:{}'.format(result))
