#  Description: 
#  ---------------

#  Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.
#  You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
#  Example:
#  Given 1->2->3->4->5->NULL,
#  return 1->3->5->2->4->NULL.
#  Note:
#  The relative order inside both the even and odd groups should remain as it was in the input.
#  The first node is considered odd, the second node even and so on ...
#  Credits:
#  Special thanks to @DjangoUnchained for adding this problem and creating all test cases.



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head == None): return None
        if (head.next == None): return head
        odd_head = head 
        odd_tail = head
        even_head = head.next
        even_tail = head.next
        curr = even_tail.next
        while True:
            if curr:
                odd_tail.next = curr
                odd_tail = curr
                curr = curr.next
            else:
                odd_tail.next = even_head
                even_tail.next = None
                return odd_head
                if curr:
                even_tail.next = curr
                even_tail = curr
                curr = curr.next
            else:
                odd_tail.next = even_head
                even_tail.next = None
                return odd_head
                                                                                    