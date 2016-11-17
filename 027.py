class Solution(object):

    def removeElement(self,  nums,  val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        il = -1
        ir = len(nums)
        while True:
            # from il+1 to ir-1,  find the first element equal to val
            find_ele = False
            while il < ir - 1:
                il += 1
                if nums[il] == val:
                    find_ele = True
                    break
            if not find_ele:
                return il + 1
            # from ir-1 to il+1,  find the first element not equal to val
            find_ele = False
            while ir > il + 1:
                ir -= 1
                if nums[ir] != val:
                    find_ele = True
                    break
            if not find_ele:
                return il
            nums[il] = nums[ir]

if __name__ == "__main__":
    a = [3, 2, 2, 3, 4, 5, 7, 8, 8, 3, 2, 3, 4, 5, 2, 4]
    # print a
    # print Solution().removeElement(a,  3)
    # print a
    # print

    a = [1]
    print a
    print Solution().removeElement(a,  1)
    print a
