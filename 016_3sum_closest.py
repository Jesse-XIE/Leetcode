class Solution(object):

    def threeSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        N = len(nums)
        if N < 3:
            return None
        nums.sort()
        min_diff = target - (nums[0] + nums[1])
        i = 0
        while i < N:
            j = i + 1
            k = N - 1
            while j < k:
                diff = target - (nums[i] + nums[j] + nums[k])
                min_diff = min(diff, min_diff)
                if diff == 0:
                    return target
                elif diff > 0:
                    j += 1
                else:
                    k -= 1
            i += 1
        return min_diff

if __name__ == "__main__":
    print Solution().threeSum([-1, 0, 1, 2, -1, -4], 10)
    assert Solution().threeSum([-1, 0, 1, 2, -1, -4], 10) == 7
