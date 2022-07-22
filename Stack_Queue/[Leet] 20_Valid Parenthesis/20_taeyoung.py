class Solution:
    def isValid(self, s: str) -> bool:
        match = {')': '(', '}': '{', ']': '['}
        stack = []

        for _char in s:
            if _char not in match:
                stack.append(_char)
            elif len(stack) == 0 or match[_char] != stack.pop():
                return False
        return len(stack) == 0