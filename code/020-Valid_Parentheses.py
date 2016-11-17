#  Description: 
#  ---------------

#  Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#  The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.



class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 == 1:
            return False
        left = ["(", "[", "{"]
        right = [")", "]", "}"]
        stack = []
        for r in s:
            if r in left:
                stack.append(r)
            elif not stack or left.index(stack[-1]) != right.index(r):
                return False
            else:
                stack.pop(-1)
        return len(stack) == 0
        