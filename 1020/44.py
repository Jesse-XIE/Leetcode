class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        a = 0
        pp = self.split_pattern(p)

    def split_pattern(self,p):
        res = []
        i0 = 0
        i1 = 0
        for i1 in range(len(p)):
            if p[i1]=='*':
                if i1>i0:
                    res.append(p[i0:i1])
                i0=i1+1
        if i0<len(p):
            res.append(p[i0:])
        return res

    def find_frist_match(self, s, index, p):
        for i0 in range(index,len(s)-len(p)+1):
            equal = True
            for i1 in range(len(p)):
                if not(p[i1]=='?' or p[i1]==s[i0+i1]):
                    equal = False
                    break
            if equal:
                return i0
        return -1

if __name__ == '__main__':
    print Solution().split_pattern('1***122*1sks*1*')
    print Solution().find_frist_match('1fkdaljgnbvsakl',0,'kl')
    print 1234*1243