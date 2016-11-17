#  Description: 
#  ---------------

#  You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.
#  For example, given:
#  s: "barfoothefoobarman"
#  words: ["foo", "bar"]
#  You should return the indices: [0,9].
#  (order does not matter).



class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(s)==0 or len(words)==0: 
            return []
        words_dict = {}
        for w in words:
            words_dict[w] = words_dict[w] + 1 if w in words_dict else 1
        len_word = len(words[0])
        result = []
        for i in range(len_word):
            i0 = i    # i0: start of search,  i: current search indice
            words_dict_curr = words_dict.copy()  ### words remains to be found
#           print 
            while i<len(s):
                word = s[i:i+len_word]
                # print words_dict_curr,i0,i
                if words_dict_curr.has_key(word):
                    if words_dict_curr[word] > 1:
                        words_dict_curr[word] -= 1
                    else:
                        words_dict_curr.pop(word)
                    if not words_dict_curr:
                        result.append(i0)
                        words_dict_curr[s[i0:i0+len_word]] = 1
                        i0 += len_word
                    i += len_word
                else:
                    if i0<i:
                        w = s[i0:i0+len_word]
                        if w not in words_dict:
                            while i0<i:
                                words_dict_curr[w] = words_dict_curr[w] + 1 if w in words_dict_curr else 1
                                i0 += len_word
                            i += len_word
                            i0 = i
                        else:    
                            words_dict_curr[w] = words_dict_curr[w] + 1 if w in words_dict_curr else 1
                            i0 += len_word
                    else:
                        i0 += len_word
                        i = i0
        return result 