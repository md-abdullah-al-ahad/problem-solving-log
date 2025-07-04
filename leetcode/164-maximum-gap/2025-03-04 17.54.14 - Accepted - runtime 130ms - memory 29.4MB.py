import heapq
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        ans = 0
        nums = sorted(nums)
        for i in range (1,len(nums)):
            comp = abs(nums[i]-nums[i-1])
            if comp>ans:
                ans = comp
        return ans
        