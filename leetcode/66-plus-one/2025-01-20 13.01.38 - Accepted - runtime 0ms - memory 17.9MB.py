class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        first_digit = digits[0]
        n = len(digits)
        for i in range (n-1,-1,-1):
            if digits[i] == 9 and carry == 1:
                digits[i] = 0
                carry = 1
            else:
                digits[i] +=1
                carry = 0
                break
        if first_digit == 9 and carry == 1:
            digits.insert(0,1)
        return digits
