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


if __name__ == '__main__':
    print Solution().combinationSum2([1,2,3],6)


