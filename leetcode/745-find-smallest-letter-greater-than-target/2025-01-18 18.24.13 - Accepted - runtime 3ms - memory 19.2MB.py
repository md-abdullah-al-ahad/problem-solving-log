class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ans = -1
        left, right = 0,len(letters)-1
        while left <= right:
            mid = left + (right-left)//2
            if letters[mid]<=target:
                left = mid + 1
            else:
                right = mid -1
                ans = letters[mid]
        return ans if ans != -1 else letters[0]
