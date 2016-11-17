class Solution(object):

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # s = [r for r in s]
        pp = p.split('*')
        head = pp.pop(0) if pp else ''
        tail = pp.pop() if pp else ''

        left, right = 0, len(s) - 1
        # match head
        if self.equal(s, 0, head):
            left = len(head)
        else:
            return False
        # match tail
        if left <= len(s) - len(tail) and self.equal(s, len(s) - len(tail), tail):
            right = len(s) - len(tail) - 1
        else:
            return False

        if '*'not in p and right >= left:
            return False
        # match the remains
        while pp:
            pattern = pp.pop(0)
            pos = self.find_first_match(s, left, right, pattern)
            if pos >= 0:
                left = pos + len(pattern)
            else:
                return False
        return True

    def find_first_match(self, s, left, right, p):
        if not p:
            return left
        for i0 in range(left, right + 2 - len(p)):
            equal = True
            for i1 in range(len(p)):
                if not(p[i1] == '?' or p[i1] == s[i0 + i1]):
                    equal = False
                    break
            if equal:
                return i0
        return -1

    def equal(self, s, left, p):
        # match p with substring of s begin at 'left'.
        if len(s[left:]) < len(p):
            return False
        for i in range(len(p)):
            if p[i] != '?' and s[i + left] != p[i]:
                return False
        return True
