#  Description: 
#  ---------------

#  Divide two integers without using multiplication, division and mod operator.
#  If it is overflow, return MAX_INT.



class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = 1
        if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0:
            sign = -1
        divisor = abs(divisor)
        dividend = abs(dividend)
        current = divisor
        current_result = 1
        result = 0
        while current <= dividend:
            current <<= 1
            current_result <<= 1
        while dividend >= divisor:
            current >>= 1
            current_result >>= 1
            if current <= dividend:
                dividend -= current
                result += current_result
        import sys
        MAX_INT = 2147483647
        if sign == 1:
            return min(MAX_INT, result)
        else:
            return -min(MAX_INT+1, result)
        