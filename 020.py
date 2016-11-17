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
        print(stack)
        for r in s:
            if r in left:
                stack.append(r)
            elif not stack or left.index(stack[-1]) != right.index(r):
                return False
            else:
                stack.pop(-1)
        return len(stack) == 0


if __name__ == "__main__":
    # assert Solution().isValid("({}){}") == True
    # assert Solution().isValid("()") == True
    print Solution().isValid("()")
    # assert Solution().isValid("}}}") == False
    # assert Solution().isValid("(((") == False
