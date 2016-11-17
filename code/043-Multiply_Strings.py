#  Description: 
#  ---------------

#  Given two numbers represented as strings, return multiplication of the numbers as a string.
#  Note:
#  The numbers can be arbitrarily large and are non-negative.
#  Converting the input string to integer is NOT allowed.
#  You should NOT use internal library such as BigInteger.



class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1=='0' or num2=='0':
            return '0'
        result = [0]*(len(num1) + len(num2) -1)
        for i,a in enumerate(num1):
            for j,b in enumerate(num2):
                result[i+j] += int(a)*int(b)
        for i in xrange(len(result)-1,0,-1):
            up,result[i] = result[i]/10,result[i]%10
            result[i-1] += up
        return ''.join([str(i) for i in result])