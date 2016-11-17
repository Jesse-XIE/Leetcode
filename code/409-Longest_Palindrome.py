#  Description: 
#  ---------------

#  Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
#  This is case sensitive, for example "Aa" is not considered a palindrome here.
#  Note:
#  Assume the length of given string will not exceed 1,010.
#  Example:
#  Input:
#  "abccccdd"
#  
#  Output:
#  7
#  
#  Explanation:
#  One longest palindrome that can be built is "dccaccd", whose length is 7.



class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        is_odd = [0 for i in range(130)]
        for r in s:
            is_odd[ord(r)] = is_odd[ord(r)]^1
        num_odd = sum(is_odd) 
        num_odd = num_odd -1 if num_odd>0 else 0
        return len(s) - num_odd
                                