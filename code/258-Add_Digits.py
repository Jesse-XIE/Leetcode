#  Description: 
#  ---------------

#  Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
#  For example:
#  Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.
#  Follow up:
#  Could you do it without any loop/recursion in O(1) runtime?
#  Show Hint
#  Credits:
#  Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.



class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if (num==0): return 0
        result = num%9
        if result == 0: result = 9
        return result
        