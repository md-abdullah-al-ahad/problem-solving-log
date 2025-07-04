class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        n = int(2e6)
        primes = [True]*(n+1)
        primes[0]=primes[1]=False
        p = 2
        while p*p<=n:
            if primes[p]:
                for i in range(p*p,n+1,p):
                    primes[i]=False
            p+=1
        ans = [-1,-1]
        least = float('inf')
        range_prime = [num for num in range(left, right + 1) if primes[num]]
        for i in range (1,len(range_prime)):
            new_least = range_prime[i]-range_prime[i-1]
            if new_least<least:
                ans[0]=range_prime[i-1]
                ans[1]=range_prime[i]
                least = new_least
        return ans
                
