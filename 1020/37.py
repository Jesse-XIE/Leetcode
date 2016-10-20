class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-pla
        ce instead.
        """
        print self.try_recursive(board, 0)
        
    def try_recursive(self, board, pos):
        ## terminatioin
        if pos>80:  return True
        i,j = pos/9, pos%9
        if board[i][j] != ".":
            return self.try_recursive(board, pos + 1)
        else:
            remains = self.find_possible_number(board, i, j)
            is_ok = False
            for r in remains:
                board[i][j] = r 
                if self.try_recursive(board, pos+1):
                    is_ok = True
                    break
            if not is_ok:  board[i][j] = "."
            return is_ok
                    
    def find_possible_number(self,board,i,j):
        row = set([board[i][k] for k in range(9) ])
        col = set([board[k][j] for k in range(9) ])
        base_i, base_j = i-i%3, j-j%3
        squ = set([board[base_i + k/3][base_j + k%3] for k in range(9) ])
        numbers = set([str(i) for i in range(1,10)])  
        return numbers - row - col - squ

if __name__ == '__main__':
    board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
    ## an evil example from http://www.extremesudoku.info/sudoku.html
    board = ["..3...8..",".9.4.6.5.","4...5...9",".7.2.3.8.","..9...4..",".1.6.9.2.","8...2...4",".4.7.1.6.","..7...3.."]
    board = [[r for r in row] for row in board]
    Solution().solveSudoku(board)
    print board


