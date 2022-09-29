'''
    2022 kakao blind 괄호 변환
    - 주어진 알고리즘 순서에 맞춰 변환 진행
'''
from collections import deque

# 올바른 순서인지 확인
def check_right(s_):
    check = []
    tmp = deque(s_)
    for i in range(len(s_)):
        check.append(tmp.popleft())
        if len(check) > 1 and ''.join(check[-2:]) == '()':
            check = check[:-2]
    if len(check) == 0:
        return True
    else:
        return False

# 균형잡힌 순서인지 확인
def check_balance(s_):
    check = 0
    for c_ in s_:
        if c_ == '(':
            check += 1
        else:
            check -= 1
    if check == 0:
        return True
    else:
        return False

# u, v로 문자열 split
def divide_str(p):
    u = ""
    v = ""
    if len(p) == 2:
        return p, v
    for i in range(0, len(p), 2):
        if check_balance(p[:i+2]):
            u = p[:i+2]
            if len(u) != len(p):
                v = p[i+2:]
            break
    return u, v

# 알고리즘 구현
def rec_check(p):
    if len(p) == 0 or check_right(p):
        return p
    u, v = divide_str(p)
    if check_right(u):
        answer = u + rec_check(v)
    else:
        answer = '(' + rec_check(v) + ')'
        for i in u[1:-1]:
            if i == ')':
                answer += '('
            else:
                answer += ')'
    return answer


def solution(p):
    return rec_check(p)