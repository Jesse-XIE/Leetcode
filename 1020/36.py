class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        ## generate rows, colums, and squares:
        rows = [[] for __ in range(9)]
        cols = rows.copy()
        squs = rows.copy()
        for i in xrange(9):
            for j in xrange(9):
                v = board[i,j] 
                if v != '.':
                    rows[i].append(v)
                    cols[j].append(v)
                    squs[i/3*3 + j/3].append(v)
        for lists in [rows,cols,squs]:
            for l in lists:
                if len(set(l)) != len(l):
                    return False
        return True
