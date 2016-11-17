class Solution(object):

    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        l = len(nums)
        i = 0
        while i < l:
            while nums[i] >= 1 and nums[i] <= l and nums[i] != i + 1:
                j = nums[i] - 1
                if nums[j] == j + 1:
                    break
                nums[i], nums[j] = nums[j], nums[i]
            i += 1
        for i, n in enumerate(nums):
            if i != n - 1:
                return i + 1
        return l + 1
if __name__ == '__main__':
    print Solution().firstMissingPositive([2, -1, 5, 6, 8, 3, 1, 10, 7])
