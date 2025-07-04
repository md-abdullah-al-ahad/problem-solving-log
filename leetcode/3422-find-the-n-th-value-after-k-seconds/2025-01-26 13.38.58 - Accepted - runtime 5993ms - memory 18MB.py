class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        mod = 1000000007
        lst = [1]*n
        for i in range (k):
            for j in range (1,len(lst)):
                lst[j]=(lst[j]%mod+lst[j-1]%mod)%mod
        return lst[n-1]