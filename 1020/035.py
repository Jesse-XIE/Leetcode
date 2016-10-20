class Solution(object):
	def searchInsert(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		### particular case
		if not nums or target<=nums[0]:
			return 0
		if target>nums[-1]:
			return len(nums)
		###
		left = 0
		right = len(nums) - 1
		while left<right-1:
			mid = (left + right) /2
			if nums[mid]>=target and nums[mid-1]<target:
				return mid
			elif nums[mid]<target:
				left = mid
			else:
				right = mid
		return right