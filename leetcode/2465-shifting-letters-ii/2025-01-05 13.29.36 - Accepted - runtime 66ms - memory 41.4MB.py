class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        l = len(s)
        lst = [0] * (l + 1)
        for shift in shifts:
            start, end, direction = shift
            if direction == 1:
                lst[start] += 1
                lst[end + 1] -= 1
            else:
                lst[start] -= 1
                lst[end + 1] += 1
        total = 0
        for i in range(l):
            total += lst[i]
            lst[i] = total
        list_s = list(s)
        for i in range(l):
            shift_needed = (lst[i] % 26 + 26) % 26
            list_s[i] = chr((ord(list_s[i]) - ord("a") + shift_needed) % 26 + ord("a"))

        return "".join(list_s)
