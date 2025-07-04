class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = float('inf')
        for num in nums:
            ans = min(ans,sum(int(i) for i in str(num)))
        return ans
