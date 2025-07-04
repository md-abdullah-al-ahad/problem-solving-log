class Solution {
public:
    char kthCharacter(int k) {
        vector<int>v;
        v.push_back(1);
        for(int i = 1;i<=9;i++){
            int j = 0;
            int n = v.size();
            for(int k = 1;k<=n;k++){
                v.push_back(v[j]+1);
                j++;
            }
        }
        return 'a' + v[k-1] - 1;
    }
};