class Solution:
    def compress(self, chars: List[str]) -> int:
        left = 0
        insert_pos = 0
        for right in range (len(chars)):
            if right+1==len(chars) or chars[right]!=chars[right+1]:
                chars[insert_pos]=chars[left]
                insert_pos+=1
                total =right-left + 1
                if total>1:
                    for digit in str(total):
                        chars[insert_pos]=str(digit)
                        insert_pos+=1
                left = right + 1
        return insert_pos
                
            