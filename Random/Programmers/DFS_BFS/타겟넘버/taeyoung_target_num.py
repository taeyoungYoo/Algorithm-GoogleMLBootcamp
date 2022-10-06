'''
    프로그래머스 타겟 넘버
    - 경우의 수를 구하는 문제
    - 주어진 배열의 길이만큼 1, -1을 곱해 더하는 경우의 수를 구한다
    - itertools 사용 중복 순열
'''
from itertools import product

def get_cand(n):
    base = [1, -1]
    return list(product(base, repeat=n))

def solution(numbers, target):
    answer = 0
    cand = get_cand(len(numbers))
    for per in cand:
        tmp = 0
        for i in range(len(per)):
            tmp += per[i] * numbers[i]
        if tmp == target:
            answer += 1
    return answer

'''
    프로그래머스 타겟 넘버
    - 경우의 수를 구하는 문제
    - 주어진 배열의 길이만큼 1, -1을 곱해 더하는 경우의 수를 구한다
    - Recursive approach
'''
answer = 0

def dfs(idx, result, target, numbers):
    global answer
    if idx == len(numbers) and result == target:
        answer += 1
        return
    elif idx == len(numbers):
        return
    dfs(idx+1, result + numbers[idx], target, numbers)
    dfs(idx+1, result - numbers[idx], target, numbers)

def solution(numbers, target):
    global answer
    dfs(0, 0, target, numbers)
    return answer