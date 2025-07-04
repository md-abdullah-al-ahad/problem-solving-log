class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        ans = float('-inf')
        for i in range (n):
            total+=nums[i]
            ans = max(total,ans)
            if total<0:
                total = 0
        return ans
