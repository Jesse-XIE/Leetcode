#  Description: 
#  ---------------

#  Given an integer, write a function to determine if it is a power of three.
#  Follow up:
#  Could you do it without using any loop / recursion?
#  Credits:
#  Special thanks to @dietpepsi for adding this problem and creating all test cases.



class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1: return False
        epsilon = 0.1**13
        import math
        err = (math.log(n)/math.log(3))%1
        if ((err < epsilon) or (1-err<epsilon)):
            return True
        else:
            return False