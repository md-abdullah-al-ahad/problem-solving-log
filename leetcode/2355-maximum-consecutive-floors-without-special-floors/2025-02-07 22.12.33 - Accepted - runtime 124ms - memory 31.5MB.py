class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        lst = sorted(special)
        ans = lst[0]-bottom
        for i in range (1,len(lst)):
            ans = max(ans,lst[i]-lst[i-1]-1)
        ans = max(ans,top-lst[len(lst)-1])
        return ans