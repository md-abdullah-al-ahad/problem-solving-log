class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        total = 0
        for i in range(k - 1):
            colors.append(colors[i])
        left = 0
        for right in range(1, len(colors)):
            if colors[right] == colors[right - 1]:
                left = right
            if right - left + 1 >= k:
                total += 1
        return total
