class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        if i == len(s):
            return 0
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        total = 0
        while i < len(s) and '0' <= s[i] <= '9':
            total = total * 10 + (ord(s[i]) - ord('0'))
            i += 1
        total *= sign
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        if total < INT_MIN:
            return INT_MIN
        if total > INT_MAX:
            return INT_MAX
        return total
