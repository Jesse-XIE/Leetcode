# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None
class Solution(object):
	def mergeTwoLists(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		dummy1,dummy2 = ListNode(0),ListNode(0)
		dummy1.next = l1
		dummy2.next = l2
		p1,p2 = dummy1,dummy2
		while True:
			if not p2.next: break
			if not p1.next:
				p1.next = p2.next
				break
			v1 = p1.next.val
			v2 = p2.next.val
			if v2<=v1:
				to_insert = p2.next
				after_insert = to_insert.next
				p1.next, to_insert.next = to_insert,p1.next
				p2.next = after_insert
				p1 = p1.next 
			else:
				p1 = p1.next
		return dummy1.next

if __name__ == "__main__":
	assert Solution().mergeTwoLists(ListNode(1), ListNode(2)).val == 1