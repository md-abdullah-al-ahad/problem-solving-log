class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        lst = [1] * n
        current_pos = 0
        for i in range(n - 1):
            count = 0
            while count < k:
                if lst[current_pos] == 1:
                    count += 1
                if count == k:
                    lst[current_pos] = 0
                    break
                current_pos = (current_pos + 1) % n
        for i in range(n):
            if lst[i] == 1:
                return i + 1
