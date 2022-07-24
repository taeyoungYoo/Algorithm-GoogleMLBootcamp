# 시은 풀이 - 38ms
class Solution(object):
    def isValid(self, s):
        # 괄호를 저장할 스택
        stack = []
        # 괄호 쌍
        pairs = {')': '(', '}': '{', ']': '['}

        for value in s:
            # 여는 괄호인 경우
            if value not in pairs:
                stack.append(value)
            # 닫는 괄호인 경우
            else:
                # 괄호 쌍이 맞는 경우
                if stack and stack[-1] == pairs[value]:
                    stack.pop()
                # 괄호 쌍이 안 맞는 경우
                else:
                    return False

        # 스택이 빈 경우 => 유효한 괄호
        return not stack