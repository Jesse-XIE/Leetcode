#  Description: 
#  ---------------

#  Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
#  For "(()", the longest valid parentheses substring is "()", which has length = 2.
#  Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.



class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack, res, s = [0], 0, ')'+s
        for i in xrange(1, len(s)):
            if s[i] == ')' and s[stack[-1]] == '(':
                stack.pop()
                res = max(res, i - stack[-1])
            else:
                stack.append(i)
        return res