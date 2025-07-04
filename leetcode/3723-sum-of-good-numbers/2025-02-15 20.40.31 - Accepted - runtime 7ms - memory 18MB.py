class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        n = len(nums)
        total = 0
        for i in range(n):
            if i - k >= 0 and i + k < n:
                if nums[i] > nums[i - k] and nums[i] > nums[i + k]:
                    total += nums[i]
            elif i - k < 0 and i + k >= n:
                total += nums[i]
            elif i - k >= 0 and i + k >= n:
                if nums[i] > nums[i - k]:
                    total += nums[i]
            elif i - k < 0 and i + k < n:
                if nums[i] > nums[i + k]:
                    total += nums[i]
        return total