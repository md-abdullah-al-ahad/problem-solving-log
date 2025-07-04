from typing import List

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        dict_pairprod = {}
        total = 0
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                if product not in dict_pairprod:
                    dict_pairprod[product] = 0
                dict_pairprod[product] += 1
        for key in dict_pairprod:
            if dict_pairprod[key] > 1:
                total += (dict_pairprod[key] * (dict_pairprod[key] - 1)) * 4
        return total
