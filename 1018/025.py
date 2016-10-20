# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None
class Solution(object):	
	def reverseKGroup(self, head, k):
		"""
		:type head: ListNode
		:type k: int
		:rtype: ListNode
		"""
		dummy = ListNode(-1)
		dummy.next = head
		pl = dummy
		p0 = pl.next
		p1 = dummy
		while True
			for i in xrange(k):
				try:
					p1 = p1.next
				except:
					return dummy.next
			try:
				pr = p1.next
			except:
				return dummy.next
			p2 = p0
			p3 = p2.next
			p4 = p3.next
			for i in xrange(k-1):
				p3.next = p2
				p2,p3,p4 = p3,p4,p4.next
			pl.next = p1
			p1.next = pr
			pl = p0
			p0 = pl.next
			p1 = pl





