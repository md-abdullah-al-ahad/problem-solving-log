class Solution {
public:
    int maxScore(vector<int>& cardPoints, int k) {
        int ans = 0;
        int cur = 0;
        for (int i = 0; i < k; i++) {
            cur += cardPoints[i];
        }
        ans = cur;
        for (int i = k - 1; i >= 0; i--) {
            cur -= cardPoints[i];
            cur += cardPoints[cardPoints.size() - k + i];
            ans = max(cur, ans);
        }
        return ans;
    }
};