// Description: 
// ---------------

// Implement pow(x, n).



class Solution {
public:
    double myPow(double x, int n) {
        double result = 1.;
        unsigned int m = abs(n);
        if (n < 0) {
            x = 1. / x;
        }
        while(m) {
            if(m & 1){
                result *= x;
            }
            m = m >> 1;
            x *= x;
        }
        return result;
    }
};