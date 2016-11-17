#  Description: 
#  ---------------

#  Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
#  The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
#  
#  A partially filled sudoku which is valid.
#  Note:
#  A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.



class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # generate rows, colums, and squares:
        rows, cols, squs = [[[] for i in range(9)] for j in range(3)]
        for i in xrange(9):
            for j in xrange(9):
                v = board[i][j]
                if v != '.':
                    rows[i].append(v)
                    cols[j].append(v)
                    squs[i/3*3 + j/3].append(v)
        for lists in [rows, cols, squs]:
            for l in lists:
                if len(set(l)) != len(l):
                    return False
        return True
        