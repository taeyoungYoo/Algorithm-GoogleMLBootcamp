#runtime: 80, memory: 14MB
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, stack = collections.Counter(s), []

        for _char in s:
            counter[_char] -= 1
            if _char in stack:
                continue
            while stack and stack[-1] > _char and counter[stack[-1]] > 0:
                stack.pop()
            stack.append(_char)
        return ''.join(stack)