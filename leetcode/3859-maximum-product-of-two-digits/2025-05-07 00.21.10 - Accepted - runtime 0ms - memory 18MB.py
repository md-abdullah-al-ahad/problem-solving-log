class Solution:
    def maxProduct(self, n: int) -> int:
        digits = []
        while n!=0:
          digits.append(n%10)
          n = n//10
        digits.sort()
        return digits[len(digits)-1]*digits[len(digits)-2]