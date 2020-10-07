"""
Reverse a singly linked list.
"""



## recrusive
class Solution:
    def reverseList(self, head):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev
