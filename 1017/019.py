# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None
	# Define this to check if it works well
	def myPrint(self):
		print(self.val)
		if self.next:
			self.next.myPrint()

class Solution(object):
	def removeNthFromEnd(self, head, n):
		"""
		:type head: ListNode
		:type n: int
		:rtype: ListNode
		"""
		helper = ListNode(0)
		p1 ,p2 = helper,helper
		helper.next = head

		for i in range(n):
			p2 = p2.next
		while p2.next:
			p2,p1 = p2.next,p1.next
		to_rm = p1.next
		p1.next = to_rm.next
		del to_rm
		return helper.next

if __name__ == "__main__":
	n5 = ListNode(5)
	n4 = ListNode(4)
	n3 = ListNode(3)
	n2 = ListNode(2)
	n1 = ListNode(1)
	n1.next = n2
	n2.next = n3
	n3.next = n4
	n4.next = n5
	result = Solution().removeNthFromEnd(n1, 5)
	result.myPrint()
