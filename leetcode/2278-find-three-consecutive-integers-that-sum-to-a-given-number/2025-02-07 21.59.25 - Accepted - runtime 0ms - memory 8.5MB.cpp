class Solution {
public:
    vector<long long> sumOfThree(long long num) {
        long long int i,j,k;
        j = num/3;
        i = j-1;
        k = j+1;
        vector<long long int>v;
        if (i+j+k == num){
            v.push_back(i);
            v.push_back(j);
            v.push_back(k);
            return v;
        }
        return v;
    }
};