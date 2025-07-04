class Solution:
    def countDigits(self, num: int) -> int:
        total=0
        str_num = str(num)
        for n in str_num:
            if num%int(n)==0:
                total+=1
        return total