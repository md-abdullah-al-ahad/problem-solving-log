class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))
        if min_index > max_index:
            min_index, max_index = max_index, min_index
        left_removals = max_index + 1
        right_removals = n - min_index
        left_right_removals = (min_index + 1) + (n - max_index)

        return min(left_removals, right_removals, left_right_removals)
