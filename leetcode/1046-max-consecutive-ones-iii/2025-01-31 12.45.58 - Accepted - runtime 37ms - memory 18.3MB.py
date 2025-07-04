class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        max_len = 0
        zero_count = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                zero_count += 1
            while zero_count > k:
                if nums[i] == 0:
                    zero_count -= 1
                i += 1
            current_len = j - i + 1
            if current_len > max_len:
                max_len = current_len
        return max_len