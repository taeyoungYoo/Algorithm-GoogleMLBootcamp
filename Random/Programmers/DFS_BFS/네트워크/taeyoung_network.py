'''
    프로그래머스 네트워크
    - 덩어리의 개수를 세는 문제
    - 1 덩어리가 곧 1 네트워크
    - DFS 사용
'''


visited = []
def dfs(node, graph):
    global visited
    visited[node] = 1
    for next in graph[node]:
        if visited[next] == 0:
            dfs(next, graph)


def solution(n, computers):
    global visited
    visited = [0] * n
    graph = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if computers[i][j] == 1:
                graph[i].append(j)
    answer = 0
    for i in range(n):
        if visited[i] == 0:
            dfs(i, graph)
            answer += 1
    return answer