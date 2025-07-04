class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        lst = []
        lst.append(0)
        for i in range(1, n + 1):
            if n % i == 0:
                lst.append(i)
        if k >= len(lst):
            return -1
        else:
            return lst[k]
