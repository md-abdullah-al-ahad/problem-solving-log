class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n1 = float('-inf')
        for num in nums:
            if num>n1:
                n1 = num
        n2 = float('-inf')
        for num in nums:
            if num>n2 and num<n1:
                n2 = num
        n3 = float('-inf')
        for num in nums:
            if num>n3 and num<n2:
                n3 = num
        if n3 == float('-inf'):
            return n1
        return n3