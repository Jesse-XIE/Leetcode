#  Description: 
#  ---------------

#  Given an array and a value, remove all instances of that value in place and return the new length.
#  Do not allocate extra space for another array, you must do this in place with constant memory.
#  The order of elements can be changed. It doesn't matter what you leave beyond the new length.
#  Example:
#  Given input array nums = [3,2,2,3], val = 3
#  Your function should return length = 2, with the first two elements of nums being 2.
#  Show Hint



class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        il = -1             # End of the clean sequence
        ir = len(nums)      # Start of the dirty sequence
        while True:
            # from il+1 to ir-1, find the first element equal to val
            find_ele = False
            while il < ir-1:
                il += 1
                if nums[il] == val:
                    find_ele = True
                    break
            if not find_ele:
                return il + 1
            # from ir-1 to il+1, find the first element not equal to val
            find_ele = False
            while ir > il+1:
                ir -= 1
                if nums[ir] != val:
                    find_ele = True
                    break
            if not find_ele:
                return il
            nums[il] = nums[ir]
        