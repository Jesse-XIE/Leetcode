# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        p0 = dummy
        while True:
            try:
                p1 = p0.next
                p2 = p1.next
                p3 = p2.next
            except:
                break
            p0.next, p1.next, p2.next = p2, p3, p1
            p0 = p1
        return dummy.next
