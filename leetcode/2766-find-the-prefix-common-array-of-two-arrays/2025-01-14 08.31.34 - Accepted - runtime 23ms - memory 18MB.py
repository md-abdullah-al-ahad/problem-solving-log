class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        lst = [0]*51
        ans = []
        for i in range (len(A)):
            lst[A[i]]+=1
            lst[B[i]]+=1
            count = 0
            for c in lst:
                if c==2:
                    count +=1
            ans.append(count)
        return ans