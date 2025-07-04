class Solution:
    def minOperations(self, nums: list[int]) -> int:
        if len(nums) < 3:
            if 0 in nums:
                return -1
            else:
                return 0
        ans = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                nums[i] = 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
                ans += 1
        if nums[-1] and nums[-2]:
            return ans
        return -1
