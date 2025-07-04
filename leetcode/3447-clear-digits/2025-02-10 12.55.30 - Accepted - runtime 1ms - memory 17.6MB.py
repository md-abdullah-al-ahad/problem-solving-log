class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        digits = "0123456789"
        for c in s:
            if c in digits:
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
            
