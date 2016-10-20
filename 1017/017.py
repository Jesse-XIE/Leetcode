class Solution(object):
	digit2letters = {
	'2': "abc",
	'3': "def",
	'4': "ghi",
	'5': "jkl",
	'6': "mno",
	'7': "pqrs",
	'8': "tuv",
	'9': "wxyz",
	} 
	def letterCombinations(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""
		if not digits: return []
		return self.l2d('',digits,[])

	def l2d(self, letters, digits, result):
		if digits:
			for s in self.digit2letters[digits[0]]:
				self.l2d(letters + s, digits[1:], result)
			return result
		else:
			result.append(''.join(letters))
			return result

if __name__ == "__main__":
	print Solution().letterCombinations("23")
	assert Solution().letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

