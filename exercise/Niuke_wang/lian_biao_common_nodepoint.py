'''
Question:
输入两个链表，找出它们的第一个公共结点。
（注意因为传入数据是链表，所以错误测试数据的提示是用其他方式显示的，保证传入数据是正确的）

'''
import os
import fire
import time
import numpy as np
import time

class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        headA = pHead1
        headB = pHead2
        def helper(head):
            l = 0
            while head:
                l += 1
                head = head.next

            return l

        if headA is None or headB is None:
            return None

        l1, l2 = helper(headA), helper(headB)

        if l1 > l2:
            p, q = headA, headB
        else:
            q, p = headA, headB

        l = abs(l1 - l2)
        while l and p:
            p = p.next
            l -= 1

        while p and q:
            if p == q:
                return p
            else:
                p, q = p.next, q.next
        return None        # write code here


if __name__=='__main__':
    inputs = [1,2,3,4,5,6,7,0]
    number = 13
    s='googgle'
    t1 = time.time()
    listA = [0,9,1,2,4]
    listB = [3,2,4]
    #rs = jumpfloor(n)
    test = Solution()
    result = test.FindFirstCommonNode(listA, listB)
    #rs = numberof1(-4)
    print("Time: {}, Results: {}".format(time.time()-t1, result))

