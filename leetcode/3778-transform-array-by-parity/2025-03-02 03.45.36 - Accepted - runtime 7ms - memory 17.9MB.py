class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if num%2==0:
                ans.append(0)
        for num in nums:
            if num%2==1:
                ans.append(1)
        return ans