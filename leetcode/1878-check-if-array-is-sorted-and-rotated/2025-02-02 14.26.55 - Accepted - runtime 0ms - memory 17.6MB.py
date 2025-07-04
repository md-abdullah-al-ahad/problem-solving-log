class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        disjoint = 0
        for i in range (n):
            if nums[i]>nums[(i+1)%n]:
                disjoint+=1
        if disjoint>1:
            return False
        else:
            return True