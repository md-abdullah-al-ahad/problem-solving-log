class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def helper(i):
            if i==n-1:
                ans.append(nums[:])
                return
            for j in range(i,n):
                nums[i],nums[j] = nums[j],nums[i]
                helper(i+1)
                nums[i],nums[j] = nums[j], nums[i]
        helper(0)
        return ans