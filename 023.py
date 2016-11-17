class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return []
        firsts = []
        results = ListNode(-1)  # dummy node
        head = results
        # get first element of all lists
        for i, l in enumerate(lists):
            if l:
                firsts.append((l.val, i))
                lists[i] = l.next
        firsts.sort(key=lambda f: f[0])

        while firsts:
            results.next = ListNode(firsts[0][0])
            results = results.next
            l_id = firsts[0][1]
            firsts.pop(0)
            l = lists[l_id]
            if l:
                self.sort_insert((l.val, l_id), firsts)
                lists[l_id] = l.next
        self.print_results(head.next)
        return head.next

    def print_results(self, results):
        p = []
        while results:
            p.append(results.val)
            results = results.next

    def sort_insert(self, ele, firsts):
        val, index = ele
        if firsts == [] or val >= firsts[-1][0]:
            firsts.append(ele)
            return
        if val <= firsts[0][0]:
            firsts.insert(0, ele)
            return
        for i in range(1, len(firsts)):
            if val <= firsts[i][0] and val > firsts[i - 1][0]:
                firsts.insert(i, ele)
                return


# using heapq
import heapq


class Solution1(object):

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
        # get first element of all lists
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

if __name__ == '__main__':
    lists = [ListNode(5), ListNode(3)]
    results = Solution().mergeKLists(lists)
