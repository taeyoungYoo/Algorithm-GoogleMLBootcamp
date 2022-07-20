# 백준 5582번, 공통 부분 문자열
# 2초 시간제한, n = 1~4000

# Pypy3로 실행
# Runtime: 3884ms, memory: 114976KB
input_a = input()
input_b = input()


def solve(str_1: str, str_2: str) -> int:
    ret = 0
    left, right = 0, 0
    lim = len(str_1)
    while left < lim and right < lim:
        sub = str_1[left:right+1]
        if sub in str_2:
            ret = max(ret, len(sub))
            right += 1
        elif left == right:
            right += 1
        else:
            left += 1
    return ret


if len(input_a) > len(input_b):
    print(solve(input_b, input_a))
else:
    print(solve(input_a, input_b))

# 아래는 DP로 해결한 풀이
# Python3로 실행
# Runtime: 444ms, memory: 240400KB
import sys


input_a = sys.stdin.readline().rstrip('\n')
input_b = sys.stdin.readline().rstrip('\n')


def solve(str_1: str, str_2: str) -> int:
    dp=[[0] * (len(str_2) + 1) for i in range(len(str_1) + 1)]
    ret = 0
    for i in range(1, len(str_1)+1):
        for j in range(1, len(str_2)+1):
            if str_1[i - 1] == str_2[j - 1]:
                dp[i][j] = dp[i-1][j-1] + 1
                ret = max(ret, dp[i][j])
    return ret

print(solve(input_a, input_b))