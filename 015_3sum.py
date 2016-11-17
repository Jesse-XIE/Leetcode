class Solution(object):

    def threeSum(self,  nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        N = len(nums)
        if N < 3:
            return []
        nums.sort()
        result = []

        def get_index(n, nums, il, ir):
            for i in xrange(il, ir + 1):
                if nums[i] == n:
                    return i
                if nums[i] > n:
                    return i - 1

        def right_shift(nums, j):
            while True:
                j += 1
                if nums[j] != nums[j - 1]:
                    break
            return min(j, len(nums))

        def left_shift(nums, j):
            while True:
                j -= 1
                if nums[j] != nums[j + 1]:
                    break
            return max(j, 0)

        try:
            id0 = get_index(0, nums, 0, N - 1)
        except:
            return []
        print nums
        i = 0
        while i <= id0:
            j = i + 1
            k = N - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j = right_shift(nums, j)
                    k = left_shift(nums, k)
                elif s > 0:
                    k = left_shift(nums, k)
                else:
                    j = right_shift(nums, j)
            i = right_shift(nums, i)
        return result

if __name__ == "__main__":
    print Solution().threeSum([-1,  0,  1,  2,  -1,  -4])
    assert Solution().threeSum(
        [-1,  0,  1,  2,  -1,  -4]) == [[-1, -1,  2], [-1,  0,  1]]
    assert Solution().threeSum([-1, -1, 3]) == []
