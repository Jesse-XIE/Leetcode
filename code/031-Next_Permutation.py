#  Description: 
#  ---------------

#  Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
#  If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
#  The replacement must be in-place, do not allocate extra memory.
#  Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
#  1,2,3 → 1,3,2
#  3,2,1 → 1,2,3
#  1,1,5 → 1,5,1



class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        i1 = len(nums)-2
        found = False
        while i1 >= 0:
            if nums[i1] < nums[i1+1]:
                found = True
                break
            i1 -= 1
        if not found:
            nums.reverse()
            return
        i2 = len(nums) - 1
        while nums[i2] <= nums[i1]:
            i2 -= 1
        nums[i2], nums[i1] = nums[i1], nums[i2]
        nums[i1+1:] = reversed(nums[i1+1:])