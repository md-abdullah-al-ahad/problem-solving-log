class Solution:
    def maxAbsoluteSum(self, nums):
        total = maxtotal = mintotal = 0
        for num in nums:
            total += num
            maxtotal = max(maxtotal, total)
            mintotal = min(mintotal, total)
        return abs(maxtotal - mintotal)
