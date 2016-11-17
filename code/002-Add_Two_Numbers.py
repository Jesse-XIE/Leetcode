#  Description: 
#  ---------------

#  You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#  Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#  Output: 7 -> 0 -> 8



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3_dummy = ListNode(0)
        l3 = l3_dummy
        lift = 0
        while l1 and l2:
            sum_temp = l1.val + l2.val + lift
            l3.next = ListNode(sum_temp % 10)
            lift = sum_temp / 10
            l3 = l3.next
            l2 = l2.next
            l1 = l1.next
        l_remain = l1 if l1 else l2
        while l_remain:
            sum_temp = l_remain.val + lift
            l3.next = ListNode(sum_temp % 10)
            lift = sum_temp / 10
            l_remain = l_remain.next
            l3 = l3.next
        if lift > 0:
            l3.next = ListNode(lift)
        return l3_dummy.next
        