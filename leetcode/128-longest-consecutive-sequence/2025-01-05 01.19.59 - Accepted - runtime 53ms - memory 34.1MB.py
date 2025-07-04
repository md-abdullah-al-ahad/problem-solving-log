class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        nums_set = set(nums)
        for num in nums_set:
            if num-1 not in nums_set:
                current_total = 1
                while (num+current_total) in nums_set:
                    current_total +=1
                ans = max(ans, current_total) 
        return ans 
        