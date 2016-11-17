// Description: 
// ---------------

// You are given an n x n 2D matrix representing an image.
// Rotate the image by 90 degrees (clockwise).
// Follow up:
// Could you do this in-place?



class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        int i_bound = n / 2 + n % 2;
        int j_bound = n / 2;
        for(int i = 0; i != i_bound; ++i){
            for(int j = 0; j != j_bound; ++j){
                swap(matrix[i][j], matrix[n - 1 - j][i]);
                swap(matrix[n - 1 - j][i], matrix[n - 1 - i][n - 1 - j]);
                swap(matrix[n - 1 - i][n - 1 - j], matrix[j][n - 1 - i]);
            }
        }
    }
};