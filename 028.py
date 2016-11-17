class Solution(object):

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if not haystack:
            return -1
        k = len(needle)
        i = 0
        while i < len(haystack):
            if haystack[i:i + k] == needle:
                return i
            try:
                c = haystack[i + k]
            except:
                return -1

            try:
                index = needle.rindex(c)
            except:
                i += k + 1
            else:
                i += k - index

        return -1
