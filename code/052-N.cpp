// Description: 
// ---------------

// Follow up for N-Queens problem.
// Now, instead outputting board configurations, return the total number of distinct solutions.



class Solution {
public:
    int totalNQueens(int n) {
        vector<bool> diag_ipj(2 * n - 1, true), diag_imj(2 * n - 1, true), col_j(n, true);
        int total = 0;
        solveRecursive(diag_ipj, diag_imj, col_j, n, 1, total);
        return total;
    }
        void solveRecursive(vector<bool> &diag_ipj, vector<bool> &diag_imj, vector<bool> &col_j, int n, int i, int &total){
        for(int j = 0; j != n; ++j){
            int ipj = i + j;
            int imj = i - j + n - 1;
            if(diag_ipj[ipj] and diag_imj[imj] and col_j[j]){
                diag_ipj[ipj] = false;
                diag_imj[imj] = false;
                col_j[j] = false;
                if(i == n){     
                    ++total;
                }
                else {
                    solveRecursive(diag_ipj, diag_imj, col_j, n, i+1, total);
                }
                diag_ipj[ipj] = true;
                diag_imj[imj] = true;
                col_j[j] = true;
            }
        }
    }
};