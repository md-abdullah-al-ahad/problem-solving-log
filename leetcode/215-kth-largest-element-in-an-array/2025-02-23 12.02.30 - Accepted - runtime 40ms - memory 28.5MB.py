import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hashmap = [0]*20005
        m = 10000
        for num in nums:
            hashmap[num+10000]+=1
        j = 0
        for i in range(20001,-1,-1):
            while hashmap[i]!=0:
                if j == k - 1:
                    return i - m
                hashmap[i]-=1
                j+=1
