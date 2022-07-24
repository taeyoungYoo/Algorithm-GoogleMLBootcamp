# 시간 초과
def solution1(str1, str2):
    while str2 in str1:
        str1 = str1.replace(str2, "")

    if str1:
        return str1
    else:
        return "FRULA"

# 784 ms
def solution2(str1, str2):
    stack, n = [], len(str2)

    for char in str1:
        stack.append(char)
        # 폭발 문자열 발견 및 제거
        if len(stack) >= n and "".join(stack[-n:]) == str2:
            for _ in range(n):
                stack.pop()

    if stack:
        return "".join(stack)
    else:
        return "FRULA"

# 초기 문자열
str1 = input()
# 폭발 문자열
str2 = input()

print(solution1(str1, str2))
print(solution2(str1, str2))