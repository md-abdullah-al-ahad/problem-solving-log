class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        cur = 0
        ans = 0
        i = 0
        for j in range(len(nums)):
            while cur & nums[j]:
                cur = cur ^ nums[i]
                i += 1
            ans = max(ans, j - i + 1)
            cur = cur | nums[j]
        return ans
