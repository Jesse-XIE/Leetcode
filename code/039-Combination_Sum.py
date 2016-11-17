#  Description: 
#  ---------------

#  Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
#  The same repeated number may be chosen from C unlimited number of times.
#  Note:
#  All numbers (including target) will be positive integers.
#  The solution set must not contain duplicate combinations.
#  For example, given candidate set [2, 3, 6, 7] and target 7,
#  A solution set is:
#  [
#    [7],
#    [2, 2, 3]
#  ]



class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()
        for index in range(len(candidates)):
            self.recursive_solve(result, [], target, index, candidates)
        return result
    def recursive_solve(self,result,curr,diff,index,c):
        if c[index] == diff:
            curr.append(c[index])
            result.append(curr)
            return
        elif c[index] > diff:
            return
        else:
            curr.append(c[index])
            diff -= c[index]
            for index in range(index,len(c)):
                self.recursive_solve(result, curr[:], diff, index, c)