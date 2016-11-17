#  Description: 
#  ---------------

#  Given a sorted array of integers, find the starting and ending position of a given target value.
#  Your algorithm's runtime complexity must be in the order of O(log n).
#  If the target is not found in the array, return [-1, -1].
#  For example,
#  Given [5, 7, 7, 8, 8, 10] and target value 8,
#  return [3, 4].



class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # special case
        if not nums or target < nums[0] or target > nums[-1]:
            return [-1, -1]
        # left boundary
        left = 0
        right = len(nums)-1
        found = False
        left_index = -1
        if nums[0] == target:
            left_index = 0
        else:
            while left <= right:
                middle = (left + right) / 2
                if nums[middle] == target:
                    if nums[middle-1] != nums[middle]:
                        left_index = middle
                        break
                    else:
                        right = middle - 1
                if nums[middle] < target:
                    left = middle + 1
                if nums[middle] > target:
                    right = middle - 1
        # right boundary
        left = 0
        right = len(nums)-1
        right_index = -1
        if nums[-1] == target:
            right_index = len(nums)-1
        else:
            while left <= right:
                middle = (left + right) / 2
                if nums[middle] == target:
                    if nums[middle+1] != nums[middle]:
                        right_index = middle
                        break
                    else:
                        left = middle + 1
                if nums[middle] < target:
                    left = middle + 1
                if nums[middle] > target:
                    right = middle - 1
        return [left_index, right_index]
        