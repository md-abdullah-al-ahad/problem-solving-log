class Solution {
public:
    bool checkPrimeFrequency(vector<int>& nums) {
        vector<bool> isPrime(101, true);
        isPrime[0] = false;
        isPrime[1] = false;
        for (int i = 2; i * i <= 101; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j < 101; j += i) {
                    isPrime[j] = false;
                }
            }
        }
        map<int, int> mpp;
        for (int i = 0; i < nums.size(); i++) {
            mpp[nums[i]]++;
        }
        for (auto it : mpp) {
            if (isPrime[it.second]) {
                return true;
            }
        }
        return false;
    }
};