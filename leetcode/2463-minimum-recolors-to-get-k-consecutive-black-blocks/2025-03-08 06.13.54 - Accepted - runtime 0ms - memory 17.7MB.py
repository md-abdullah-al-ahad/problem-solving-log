class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = float("inf")
        cur_white = 0
        for i in range(len(blocks)):
            if blocks[i] == "W":
                cur_white += 1
            if i >= k - 1:
                ans = min(cur_white, ans)
                if blocks[i - k + 1] == "W":
                    cur_white -= 1
        return ans
