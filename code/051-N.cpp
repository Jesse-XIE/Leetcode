// Description: 
// ---------------

// The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
// Given an integer n, return all distinct solutions to the n-queens puzzle.
// Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
// For example,
// There exist two distinct solutions to the 4-queens puzzle:
// [
//  [".Q..",  // Solution 1
//   "...Q",
//   "Q...",
//   "..Q."],
// 
//  ["..Q.",  // Solution 2
//   "Q...",
//   "...Q",
//   ".Q.."]
// ]



class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<bool> diag_ipj(2 * n - 1, true), diag_imj(2 * n - 1, true), col_j(n, true);
        vector<int> j_list;
        vector<vector<string>> results;
        solveRecursive(diag_ipj, diag_imj, col_j, j_list, n, results);
        return results;
    }
        void solveRecursive(vector<bool> &diag_ipj, vector<bool> &diag_imj, vector<bool> &col_j, vector<int> &j_list, int n, vector<vector<string>> &results){
        int i = j_list.size() + 1;
        for(int j = 0; j != n; ++j){
            int ipj = i + j;
            int imj = i - j + n - 1;
            if(diag_ipj[ipj] and diag_imj[imj] and col_j[j]){
                diag_ipj[ipj] = diag_imj[imj] = col_j[j] = false;
                j_list.push_back(j);
                if(j_list.size() == n){     // push back current result in required format
                    vector<string> result;
                    for(auto &jj: j_list){
                        string row(n, '.');
                        row[jj] = 'Q';
                        result.push_back(row);
                    }
                    results.push_back(result);
                }
                else {
                    solveRecursive(diag_ipj, diag_imj, col_j, j_list, n, results);
                }
                j_list.pop_back();
                diag_ipj[ipj] = diag_imj[imj] = col_j[j] = true;
            }
        }
    }
};