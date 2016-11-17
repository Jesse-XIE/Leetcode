#  Description: 
#  ---------------

#  Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy1 = ListNode(0)
        dummy1.next = l1
        p1, p2 = dummy1, l2
        while True:
            if not p2:
                break
            if not p1.next:
                p1.next = p2
                break
            if p1.next.val >= p2.val:
                after_insert = p2.next
                p1.next, p2.next = p2, p1.next
                p2, p1 = after_insert, p1.next
            else:
                p1 = p1.next
        return dummy1.next
        