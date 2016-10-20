class Solution(object):
	def removeDuplicates(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if not nums: return []
		if len(nums) ==1 : return nums
		i0,i1 = 0,0
		while i1<len(nums)-1:
			nums[i0] = nums[i1]
			i0 += 1
			i1 += 1
			while i1<len(nums) and nums[i1] == nums[i1-1]:
				i1 += 1
		if len(nums)>1 and nums[-1] != nums[-2]:
			nums[i0] = nums[-1]
			i0 +=1
		return i0 

	def removeDuplicates2(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if not nums: return 0
		i0 = 0
		for i1 in range(1,len(nums)):
			if nums[i1] != nums[i0]:
				i0 += 1
				nums[i0] = nums[i1]
		return i0+1




if __name__ == "__main__":
	a = [1,1]
	print a
	print Solution().removeDuplicates2(a)
	print a
	print 
	a = [1,2,3,3,4,4,5,5,5,6]
	print a
	print Solution().removeDuplicates2(a)
	print a
	print 
	a = [1,1,2]
	print a
	print Solution().removeDuplicates2(a)
	print a
	print 
	a = [1]
	print a
	print Solution().removeDuplicates2(a)
	print a
	print 





						



