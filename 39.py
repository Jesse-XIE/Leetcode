class Solution(object):

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()
        for index in len(candidates):
            self.recursive_solve(result, [], target, index, candidates)
        return result

    def recursive_solve(self, result, curr, diff, index, c):
        if c[index] == diff:
            curr.append(c[index])
            result.append(curr)
            return
        elif c[index] > diff:
            return
        else:
            curr.append(c[index])
            diff -= c[index]
            for index in range(index, len(c)):
                self.recursive_solve(result, curr[:], diff, index, c)

if __name__ == '__main__':
    print Solution().combinationSum([1, 2, 3], 7)
