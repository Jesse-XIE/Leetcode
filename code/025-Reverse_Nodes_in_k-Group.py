#  Description: 
#  ---------------

#  Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#  If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
#  You may not alter the values in the nodes, only nodes itself may be changed.
#  Only constant memory is allowed.
#  For example,
#  Given this linked list: 1->2->3->4->5
#  For k = 2, you should return: 2->1->4->3->5
#  For k = 3, you should return: 3->2->1->4->5



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        tail_sub = dummy
        head_sub = head
        while True:
            for i in xrange(k):
                if head_sub:
                    head_sub = head_sub.next
                else:
                    return dummy.next
            pl = head_sub
            pm = head
            temp = head
            pr = head.next
            for i in xrange(k-1):
                pm.next = pl
                pl, pm, pr = pm, pr, pr.next
            pm.next = pl
            tail_sub.next = pm
            tail_sub = temp
            head = head_sub
        return dummy.next