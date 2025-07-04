class Solution {
public:
    string shiftingLetters(string s, vector<int>& shifts) {
        int n = shifts.size();
        for(int i = 0;i<n;i++){
            shifts[i]= shifts[i]%26;
        }
        for (int i = n - 2; i >= 0; i--) {
            shifts[i] += shifts[i + 1];
            shifts[i] = shifts[i]%26;
        }
        for (int i = 0; i < n; i++) {
            int val = s[i] - 'a';
            val += shifts[i];
            val = val % 26;
            s[i] = 'a' + val;
        }
        return s;
    }
};