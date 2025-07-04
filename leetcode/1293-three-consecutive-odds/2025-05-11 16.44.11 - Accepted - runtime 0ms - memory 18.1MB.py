class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        freq = 0
        for i in range (len(arr)):
            if arr[i]%2==1:
                freq+=1
                if freq == 3:
                    return True
            else:
                freq = 0
        return False