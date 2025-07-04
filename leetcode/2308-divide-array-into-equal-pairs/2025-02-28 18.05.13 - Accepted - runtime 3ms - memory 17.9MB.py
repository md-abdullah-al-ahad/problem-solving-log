from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hashmap = Counter(nums)
        for freq in hashmap.values():
            if freq % 2 != 0:
                return False
        return True
