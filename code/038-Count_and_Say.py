#  Description: 
#  ---------------

#  The count-and-say sequence is the sequence of integers beginning as follows:
#  1, 11, 21, 1211, 111221, ...
#  1 is read off as "one 1" or 11.
#  11 is read off as "two 1s" or 21.
#  21 is read off as "one 2, then one 1" or 1211.
#  Given an integer n, generate the nth sequence.
#  Note: The sequence of integers will be represented as a string.



class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s,s_new = ['1'],[]
        for i in range(n-1):
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
        return ''.join(s)
        