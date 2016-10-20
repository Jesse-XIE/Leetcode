class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums)<2: return 
        i1 = len(nums)-2
        found = False
        while i1>=0 :
            if nums[i1]<nums[i1+1]:
                found = True
                break
            i1 -= 1
        if not found:
            nums.reverse()
            return

        i2 = len(nums) - 1
        while nums[i2]<=nums[i1]:
            i2 -= 1

        nums[i2],nums[i1] = nums[i1],nums[i2]
        nums[i1+1:] = reversed(nums[i1+1:])

        






