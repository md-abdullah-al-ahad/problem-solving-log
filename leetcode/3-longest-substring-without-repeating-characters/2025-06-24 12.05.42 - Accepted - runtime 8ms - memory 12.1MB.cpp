class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        map<char, int> alpha;
        int i = 0, j = 0;
        int n = s.size();
        int ans = 0;
        while (j < n) {
            alpha[s[j]]++;
            while (alpha[s[j]] > 1) {
                alpha[s[i]]--;
                i++;
            }
            ans = max(ans, j - i + 1);
            j++;
        }
        return ans;
    }
};