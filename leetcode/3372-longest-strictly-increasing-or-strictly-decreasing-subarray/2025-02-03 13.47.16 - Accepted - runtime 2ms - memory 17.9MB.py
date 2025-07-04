class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = 0
        current_longest = 1
        for i in range (len(nums)-1):
            if nums[i]<nums[i+1]:
                current_longest+=1
            else:
                ans = max(current_longest,ans)
                current_longest = 1
        ans = max(current_longest,ans)
        current_longest = 1
        for i in range (len(nums)-1):
            if nums[i]>nums[i+1]:
                current_longest+=1
            else:
                ans = max(current_longest,ans)
                current_longest = 1
        ans = max(current_longest,ans)
        return ans