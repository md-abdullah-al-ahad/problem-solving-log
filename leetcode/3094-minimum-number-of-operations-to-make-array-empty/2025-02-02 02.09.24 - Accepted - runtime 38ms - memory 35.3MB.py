class Solution:
    def minOperations(self, nums: List[int]) -> int:
        from collections import Counter
        total = 0
        freq = Counter(nums)
        for count in freq.values():
            if count == 1:
                return -1
        for count in freq.values():
            total+=count//3
            if count%3!=0:
                total+=1
        return total