#  Description: 
#  ---------------

#  Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
#  Each number in C may only be used once in the combination.
#  Note:
#  All numbers (including target) will be positive integers.
#  The solution set must not contain duplicate combinations.
#  For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
#  A solution set is:
#  [
#    [1, 7],
#    [1, 2, 5],
#    [2, 6],
#    [1, 1, 6]
#  ]



class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        self.recursive_solve(result,[],target,0,sorted(candidates))
        return result
    def recursive_solve(self,result,curr,diff,index,c):
        for i in range(index,len(c)):
            n = c[i]
            nl = c[i-1] if i>index else -1
            if n==diff and n!=nl:
                result.append(curr+[n])
            elif n<diff and n!=nl:
                self.recursive_solve(result, curr+[n], diff-n, i+1, c)
            elif n>diff:
                break
        