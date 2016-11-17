#  Description: 
#  ---------------

#  Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution():
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return []
        heap = []
        results = ListNode(-1)  # dummy node
        head = results
        # Get first element of all lists
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, node))
        while heap:
            node = heapq.heappop(heap)[1]
            results.next = node
            results = results.next
            if node.next:
                heapq.heappush(heap, (node.next.val, node.next))
        return head.next
        