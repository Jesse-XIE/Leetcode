#  Description: 
#  ---------------

#  Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
#  Note: The solution set must not contain duplicate quadruplets.
#  For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.
#  
#  A solution set is:
#  [
#    [-1,  0, 0, 1],
#    [-2, -1, 1, 2],
#    [-2,  0, 0, 2]
#  ]



class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        result = []
        results = []
        nums.sort()
        self.Nsum(nums, 4, target, result, results)
        return results
    def Nsum(self, nums, N, target, result, results):
        if len(nums) < N:
            return
        if target < nums[0]*N or target > nums[-1]*N:
            return
        if N == 2:
            i = 0
            j = len(nums) - 1
            while i < j:
                s = nums[i] + nums[j]
                if s == target:
                    results.append(result + [nums[i], nums[j]])
                    j = self.left_shift(nums, j)
                    i = self.right_shift(nums, i)
                elif s > target:
                    j = self.left_shift(nums, j)
                else:
                    i = self.right_shift(nums, i)
        else:
            i = 0
            id_average = self.get_index((target/N), nums, 0, len(nums)-1)
            while i < min(len(nums)-N+1, id_average+1):
                self.Nsum(
                    nums[i+1:], N-1, target-nums[i], result+[nums[i]], results)
                i = self.right_shift(nums, i)
    def right_shift(self, nums, j):
        while True:
            j += 1
            if (j == len(nums)-1 or nums[j] != nums[j-1]):
                return j
    def left_shift(self, nums, j):
        while True:
            j -= 1
            if (j == 0 or nums[j] != nums[j+1]):
                return j
    def get_index(self, n, nums, il, ir):
        for i in xrange(il, ir+1):
            if nums[i] == n:
                return i
            if nums[i] > n:
                return i-1
        