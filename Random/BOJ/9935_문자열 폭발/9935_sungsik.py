s = 'mirkovC4nizCC44'
explode = 'C4'

# 풀이 3. stack + del : 메모리 42020 kb, 시간 508 ms
stack = []
for i in s:
    stack.append(i)
    if stack[-1] == explode[-1] and ''.join(stack[-len(explode):]) == explode:
        del stack[-len(explode):]
print('FRULA' if ''.join(stack) == '' else ''.join(stack))


# 풀이 1. re.sub : 런타임 에러 (NameError)
# while explode in s:
#     s = re.sub(explode, '', s)
#
# print('FRULA' if s == '' else s)


# 풀이 2. stack + replace : 시간 초과
# stack = ''
# for i in s:
#     stack += i
#     if stack[-1] == explode[-1] and stack[-len(explode):] == explode:
#         stack = stack.replace(stack[-len(explode):], '')
# print('FRULA' if stack == '' else stack)
