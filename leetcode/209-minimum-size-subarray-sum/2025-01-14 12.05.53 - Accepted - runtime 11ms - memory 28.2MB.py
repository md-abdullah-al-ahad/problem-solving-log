class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float("inf")
        left = 0
        right = 0
        current_sum = 0
        while(right<len(nums)):
            current_sum +=nums[right]
            while current_sum>=target:
                if right - left + 1 < ans:
                    ans = right - left + 1
                current_sum-=nums[left]
                left+=1
            right+=1
        if ans == float("inf"):
            return 0
        else:
            return ans