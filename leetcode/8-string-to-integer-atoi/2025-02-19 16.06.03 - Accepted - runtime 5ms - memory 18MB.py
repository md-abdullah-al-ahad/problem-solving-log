class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s)==0:
            return 0
        for j in range (len(s)):
            if s[j]==" ":
                continue
            else:
                break
        i = j
        sign = 0
        if s[i]=="-":
            sign = -1
            i+=1
        elif s[i]=="+":
            sign = 1
            i+=1
        else:
            sign = 1
        numbers="0123456789"
        main_number = []
        flag = 0
        while i<len(s):
            if s[i] in numbers:
                if s[i] != "0":
                    flag = 1
                    main_number.append(s[i])
                else:
                    if flag==1:
                        main_number.append(s[i])
            else:
                break
            i+=1
        total = 0
        for i in range (len(main_number)):
            total = total*10 + int(main_number[i])
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        if total * sign < INT_MIN:
            return INT_MIN
        elif total * sign > INT_MAX:
            return INT_MAX
        else:
            return total * sign