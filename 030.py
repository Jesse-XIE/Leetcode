class Solution(object):

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        # if len(s)==0 or len(words)==0:
        # 	return []
        words_dict = {}
        for w in words:
            if not words_dict.has_key(w):
                words_dict[w] = 1
            else:
                words_dict[w] += 1
        len_word = len(words[0])
        result = []
        for i in range(len_word):
            words_dict_curr = words_dict
            while i < len(s):
                word = s[i:i + len_word]
                if word in words_dict_curr:
                    if words_dict_curr[word] > 1:
                        words_dict_curr[word] -= 1
                    else:
                        words_dict_curr.pop(word)
                    if not words_dict_curr:
                        result.append[i - len_word * (len(words) - 1)]
                        words_dict_curr = words_dict
        return result

# my second solution


class Solution(object):

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        if len(s) == 0 or len(words) == 0:
            return []
        words_dict = {}
        for w in words:
            words_dict[w] = words_dict[w] + 1 if w in words_dict else 1
        len_word = len(words[0])
        result = []
        for i in range(len_word):
            i0 = i    # i0: start of search,  i: current search indice
            words_dict_curr = words_dict.copy()  # words remains to be found
# 			print
            while i < len(s):
                word = s[i:i + len_word]
                # print words_dict_curr,i0,i
                if words_dict_curr.has_key(word):
                    if words_dict_curr[word] > 1:
                        words_dict_curr[word] -= 1
                    else:
                        words_dict_curr.pop(word)
                    if not words_dict_curr:
                        result.append(i0)
                        words_dict_curr[s[i0:i0 + len_word]] = 1
                        i0 += len_word
                    i += len_word
                else:
                    if i0 < i:
                        w = s[i0:i0 + len_word]
                        words_dict_curr[w] = words_dict_curr[
                            w] + 1 if w in words_dict_curr else 1
                        i0 += len_word
                    else:
                        i0 += len_word
                        i = i0
        return result
