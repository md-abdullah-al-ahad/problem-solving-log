from collections import defaultdict
from sortedcontainers import SortedList
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        hashmap = defaultdict(SortedList)
        for i in range (len(nums)):
            digit_sum = sum(int(digit) for digit in str(nums[i]))
            hashmap[digit_sum].add(nums[i])
        ans = -1
        for key, value in (hashmap.items()):
            if len(value) > 1:
                ans = max(sum(value[-2:]),ans)
        return ans

