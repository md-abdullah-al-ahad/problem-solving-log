class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        highest = max(nums)
        lowest = min(nums)
        for num in nums:
            if num!=highest and num!=lowest:
                return num
        return -1