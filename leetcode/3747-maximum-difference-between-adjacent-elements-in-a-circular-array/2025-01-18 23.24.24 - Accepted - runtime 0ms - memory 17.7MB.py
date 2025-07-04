class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        current_max = abs(nums[0]-nums[len(nums)-1])
        for i in range (len(nums)-1):
            if current_max< abs(nums[i]-nums[i+1]):
                current_max= abs(nums[i]-nums[i+1])
        return current_max