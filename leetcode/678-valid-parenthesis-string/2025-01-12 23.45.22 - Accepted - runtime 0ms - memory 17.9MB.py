class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        asterisk_stack = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == '*':
                asterisk_stack.append(i)
            else:
                if stack:
                    stack.pop()
                elif asterisk_stack:
                    asterisk_stack.pop()
                else:
                    return False
        while stack and asterisk_stack:
            if stack[-1] < asterisk_stack[-1]:
                stack.pop()
                asterisk_stack.pop()
            else:
                return False
        
        return len(stack) == 0
