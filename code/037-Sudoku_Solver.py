#  Description: 
#  ---------------

#  Write a program to solve a Sudoku puzzle by filling the empty cells.
#  Empty cells are indicated by the character '.'.
#  You may assume that there will be only one unique solution.
#  
#  A sudoku puzzle...
#  
#  ...and its solution numbers marked in red.



class Solved(Exception):
    def __init__(self):
        self.msg = "Found Soduku solution!!"
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-pla
        ce instead.
        """
        try:
            self.try_recursive(board, 0)
        except Solved:
            pass
    def try_recursive(self, board, pos):
        # terminatioin
        if pos == 81:
            raise Solved()
        i, j = pos/9, pos % 9
        if board[i][j] != ".":
            return self.try_recursive(board, pos+1)
        else:
            remains = self.find_possible_number(board, i, j)
            for r in remains:
                board[i][j] = r
                self.try_recursive(board, pos+1)
            board[i][j] = "."
    def find_possible_number(self, board, i, j):
        row = set([board[i][k] for k in range(9)])
        col = set([board[k][j] for k in range(9)])
        base_i, base_j = i - i % 3, j - j % 3
        squ = set([board[base_i + k/3][base_j + k % 3] for k in range(9)])
        numbers = [str(n) for n in range(1, 10) if str(n) not in (row | col | squ)]
        return numbers