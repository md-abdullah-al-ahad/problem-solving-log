class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            num = abs(nums[i])
            index = num - 1
            if nums[index] < 0:
                ans.append(num)
            nums[index] *= -1
        return ans
