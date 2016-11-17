#  Description:
#  ---------------

#  Implement strStr().
# Returns the index of the first occurrence of needle in haystack, or -1
# if needle is not part of haystack.


class Solution(object):
    # Implemention of KMP algorithm

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        i, j = 0, 0
        n, m = len(haystack), len(needle)
        overlap = self.calc_overlap(needle)
        while j < m and i <= (n - m):
            if haystack[i + j] == needle[j]:
                j += 1
            else:
                if j == 0:
                    i = i + 1
                else:
                    i = i + j - overlap[j - 1]
                    j = overlap[j - 1]
        return -1 if i > (n - m) else i

    def calc_overlap(self, needle):
        """
        overlap[j]: Length of the longest words which is  suffix of needle[:j]
        and prefix of needle
        """
        m = len(needle)
        overlap = [-1] * (m + 1)
        for i in xrange(0, m):
            overlap[i + 1] = overlap[i] + 1
            while overlap[i + 1] > 0 and needle[i] != needle[overlap[i + 1] - 1]:
                overlap[i + 1] = overlap[overlap[i + 1] - 1] + 1
        return overlap[1:]
