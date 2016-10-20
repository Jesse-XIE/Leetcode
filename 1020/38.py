class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s,s_new = ['1'],[]
        for i in range(n):
	        p0,p1 = 0,0
        	# print s
        	while p1<len(s)-1:
        		if s[p1]!=s[p1+1]:
        			s_new.extend([str(p1-p0+1),s[p1]])
        			p1 += 1
        			p0 = p1
        		else:
        			p1 += 1
        	s_new.extend([str(p1-p0+1),s[p1]])
        	s,s_new = s_new,[]	        
        	# print s
        return ''.join(s)
if __name__ == '__main__':
	print Solution().countAndSay(14)
