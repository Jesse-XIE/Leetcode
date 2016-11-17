#  Description: 
#  ---------------

#  Suppose a sorted array is rotated at some pivot unknown to you beforehand.
#  (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#  You are given a target value to search. If found in the array return its index, otherwise return -1.
#  You may assume no duplicate exists in the array.



class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        left = 0
        right = len(nums) - 1
        while left < right-1:
            # termination
            middle = (left + right)/2
            if nums[middle] >= nums[left]:
                if target >= nums[left] and target <= nums[middle]:
                    right = middle
                else:
                    left = middle
            else:
                if target <= nums[right] and target >= nums[middle]:
                    left = middle
                else:
                    right = middle
        if target == nums[left]:
            return left
        elif target == nums[right]:
            return right
        else:
            return -1