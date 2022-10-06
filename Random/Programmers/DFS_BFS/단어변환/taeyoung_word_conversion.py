'''
    프로그래머스 단어 변환
    - words의 단어로 변환하며 target과 일치하는게 있는지 확인
    - 주어진 words 중 변환 가능함을 확인 후 그래프 만들기
    - words 중 begin이 변환할 수 있는 모든 후보를 찾은 후 최단거리
    - 결과 중 최소값 리턴
'''
from collections import deque

graph = []


# 최단거리 반환 함수 -> BFS 활용
def find_route(start, target, lim):
    q = deque()
    q.append((start, 1))
    visited = [0] * lim
    while q:
        node, cost = q.popleft()
        if node == target:
            break
        visited[node] = 1
        for next in graph[node]:
            if visited[next] == 0:
                q.append((next, cost+1))
    return cost


# 두 str 비교 후 변환 가능한지 확인
def comp_str(a, b):
    n = len(a)
    count = 0
    for i in range(n):
        if a[i] == b[i]:
            count += 1
    if count == n-1:
        return True
    return False


def solution(begin, target, words):
    if target not in words:
        return 0

    global graph
    lim = len(words)
    # 그래프 찾기
    graph = [[] for _ in range(lim)]
    for i in range(lim):
        for j in range(i+1, lim):
            if comp_str(words[i], words[j]):
                graph[i].append(j)
                graph[j].append(i)
    cand = []
    target = words.index(target)
    # begin이 변환될 수 있는 모든 후보군 찾기
    for i in range(lim):
        if comp_str(begin, words[i]):
            cand.append(i)
    # 최소값 비교니 answer을 worst case에서 여유있는 55로 설정
    answer = 55
    # 각 후보 word에 대해 최단거리 구해서 global 최단거리 찾기
    for node in cand:
        route = find_route(node, target, lim)
        if route < answer:
            answer = route
    # 결과 리턴
    if answer != 55:
        return answer
    else:
        return 0