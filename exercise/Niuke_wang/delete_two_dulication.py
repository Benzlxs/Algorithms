'''
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5

'''

import time

class Solution:
	def deleteDuplication(self, pHead):
        first = ListNode(-1)
        first.next = pHead
        curr = pHead
        last = first
        while curr and curr.next:
            if curr.val != curr.next.val:
                curr = curr.next
                last = last.next
            else:
                val = curr.val
                while curr and curr.val == val:
                    curr = curr.next
                last.next = curr
        return first.next


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

