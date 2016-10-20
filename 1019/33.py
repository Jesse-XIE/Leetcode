class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        if len(nums)==1:
            if nums[0]==target:
                return 0
            else:
                return -1

        left = 0 
        right = len(nums) - 1
        while left<right-1:
            ## termination
            middle = (left + right)/2
            if nums[middle]>=nums[left]:
                if target >= nums[left] and target<=nums[middle]:
                    right = middle
                else:
                    left = middle
            else:
                if target <= nums[right] and target>=nums[middle]:
                    left = middle
                else: 
                    right = middle
        if target == nums[left]: 
            return left
        elif target == nums[right]:
            return right
        else:
            return -1
