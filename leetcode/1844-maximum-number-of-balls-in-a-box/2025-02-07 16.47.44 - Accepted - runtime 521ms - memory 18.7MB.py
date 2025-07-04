class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        def sum_of_digits(n):
            return sum(int(digit) for digit in str(n))
        lst = [0]*100010
        for i in range(lowLimit,highLimit+1):
            lst[sum_of_digits(i)]+=1
        return max(lst)