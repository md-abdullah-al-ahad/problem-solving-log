class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = 0
        count_zero = 0
        max_len = 0
        for j in range (len(nums)):
            if nums[j]==0:
                count_zero+=1
            while count_zero>1:
                if nums[i]==0:
                    count_zero-=1
                i+=1
            current_len = j - i
            if current_len>max_len:
                max_len=current_len
        return max_len