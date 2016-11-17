#  Description: 
#  ---------------

#  Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#  You may assume no duplicates in the array.
#  Here are few examples.
#  [1,3,5,6], 5 → 2
#  [1,3,5,6], 2 → 1
#  [1,3,5,6], 7 → 4
#  [1,3,5,6], 0 → 0



class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # particular case
        if not nums or target <= nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        ###
        left = 0
        right = len(nums) - 1
        while left < right-1:
            mid = (left + right) / 2
            if nums[mid] >= target and nums[mid-1] < target:
                return mid
            elif nums[mid] < target:
                left = mid
            else:
                right = mid
        return right