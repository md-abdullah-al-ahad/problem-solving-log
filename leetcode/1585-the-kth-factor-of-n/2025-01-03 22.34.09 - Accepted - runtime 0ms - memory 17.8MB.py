class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factor = 0 
        for i in range(1, int(sqrt(n) + 1)):
            if n % i == 0:
                factor += 1
            if factor == k:
                return i
        for j in range(int(sqrt(n) + 1), 0, -1):
            if n % j == 0 and n // j != i:
                factor += 1
            if factor == k:
                return n // j

        return -1