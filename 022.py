class Solution(object):

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        results = []
        self.generate_tree('', results, n, n)
        return results

    def generate_tree(self, result, results, nleft, nright):
        if nleft == 0:
            results.append(result + ')' * nright)
            return
        if nleft > 0:
            self.generate_tree(result + '(', results, nleft - 1, nright)
        if nright > nleft:
            self.generate_tree(result + ')', results, nleft, nright - 1)

if __name__ == "__main__":
    print(Solution().generateParenthesis(3))
