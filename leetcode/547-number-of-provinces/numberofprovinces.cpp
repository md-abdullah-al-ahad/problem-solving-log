class Solution {
public:
    void dfs(vector<vector<int>>& isConnected, vector<int>& vis, int node,
             int n) {
        vis[node] = 1;
        for (int i = 0; i < n; i++) {
            if (isConnected[node][i] == 1 && vis[i] == 0) {
                dfs(isConnected, vis, i, n);
            }
        }
    }
    int findCircleNum(vector<vector<int>>& isConnected) {
        int n = isConnected.size();
        int total = 0;
        vector<int> vis(n, 0);
        for (int i = 0; i < n; i++) {
            if (vis[i] == 0) {
                total += 1;
                dfs(isConnected, vis, i, n);
            }
        }
        return total;
    }
};