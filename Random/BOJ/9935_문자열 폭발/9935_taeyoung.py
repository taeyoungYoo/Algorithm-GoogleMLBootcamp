# BOJ 9935 문자열 폭발
# 1 <= s <= 1,000,000, 2초 시간제한
# O(N^2)보다 작게 풀어야 한다
s = input()

stack = []
check = list(input())
limit = len(check)
# O(len(s) * len(check)
for _char in s:
    stack.append(_char)
    while len(stack) >= limit and stack[-limit:] == check:
        for i in range(limit):
            stack.pop()
if stack:
    print(''.join(stack))
else:
    print("FRULA")