class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = 0
        total_sum = sum(nums)
        left_sum = 0
        l = len(nums)
        for i in range(l - 1):
            left_sum += nums[i]
            if left_sum >= total_sum - left_sum:
                total = total + 1
        return total
