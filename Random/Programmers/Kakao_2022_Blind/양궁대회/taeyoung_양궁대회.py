from itertools import combinations_with_replacement as cwr
import collections

def solution(n, info):
    answer = []
    info = info[::-1]
    max_diff = -1
    for comb in cwr(range(0, 11), n):
        ryan = 0
        apeach = 0
        tmp = [0] * 11
        comb = collections.Counter(comb)
        for i in range(11):
            if comb[i] > info[i]:
                ryan += i
            elif info[i] != 0:
                apeach += i
            tmp[i] = comb[i]
        if ryan > apeach:
            if ryan - apeach > max_diff:
                max_diff = ryan - apeach
                answer = tmp
    if max_diff == -1:
        return [-1]
    else:
        return answer[::-1]