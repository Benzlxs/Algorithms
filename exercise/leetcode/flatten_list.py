"""
You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.

"""



## recrusive
def child_parse(head):
    prev = None
    while head:
        if head.child:
            tail = child_parse(head.child)
            head.child.prev = head
            # change tail node next
            tail.next = head.next
            if head.next:
                head.next.prev = tail
            head.next = head.child
            head.child = None
            head = tail
        prev = head
        head = head.next
    return prev


class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        child_parse(head)
        return head
