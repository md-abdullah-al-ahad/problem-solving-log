from collections import defaultdict
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        hashmap = defaultdict(list)
        for num in nums:
            digit_sum = sum(int(digit) for digit in str(num))
            hashmap[digit_sum].append(num)
        ans = -1
        for key, value in hashmap.items():
            if len(value) > 1:
                max1, max2 = float('-inf'), float('-inf')
                for num in value:
                    if num > max1:
                        max2 = max1
                        max1 = num
                    elif num > max2:
                        max2 = num
                ans = max(ans, max1 + max2)
        return ans
