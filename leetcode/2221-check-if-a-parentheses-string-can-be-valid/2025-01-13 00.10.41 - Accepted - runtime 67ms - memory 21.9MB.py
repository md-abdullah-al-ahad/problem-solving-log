class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 == 1:
            return False
        stack_locked = []
        stack_unlocked = []
        for i in range(n):
            if locked[i] == '0':
                stack_unlocked.append(i)
            elif s[i] == '(':
                stack_locked.append(i)
            else:
                if stack_locked:
                    stack_locked.pop()
                elif stack_unlocked:
                    stack_unlocked.pop()
                else:
                    return False
        while stack_locked and stack_unlocked:
            if stack_locked[-1] < stack_unlocked[-1]:
                stack_locked.pop()
                stack_unlocked.pop()
            else:
                return False
        return len(stack_locked) == 0
