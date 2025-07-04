class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lst = [0]*len(nums)
        total_product = 1
        total_product_without_zero = 1
        total_zero = 0
        for i in nums:
            total_product = total_product* i
            total_product_without_zero*=(i if i!=0 else 1)
            total_zero+=(1 if i == 0 else 0)
        if total_zero > 1:
            return lst
        if total_zero == 1:
            return [total_product_without_zero if x == 0 else 0 for x in nums]
        return [total_product//x for x in nums]
        