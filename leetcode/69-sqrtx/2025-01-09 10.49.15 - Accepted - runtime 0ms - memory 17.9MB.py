class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while(left<=right):
            mid = left + (right-left)//2
            if mid*mid == x:
                return int(mid)
            elif mid*mid<x:
                left = mid + 1
            else:
                right = mid - 1
        return int(right)
        