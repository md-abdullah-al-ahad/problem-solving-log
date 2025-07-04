class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        lst = [-1]*(n+1)
        def helper(n):
            if n<0:
                return 0
            if lst[n]!=-1:
                return lst[n]
            lst[n] =  max(helper(n-1),nums[n]+helper(n-2))
            return lst[n]
        return helper(n-1)