class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        part_len = len(part)

        for char in s:
            stack.append(char)
            if (
                len(stack) >= part_len
                and "".join(stack[len(stack) - part_len : len(stack)]) == part
            ):
                del stack[len(stack) - part_len : len(stack)]

        return "".join(stack)
