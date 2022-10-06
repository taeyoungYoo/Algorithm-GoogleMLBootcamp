'''
    프로그래머스 여행 루트
    - 알파벳 순으로 탐색 루트 반환
    - 그래프 정렬 후 DFS 탐색
'''
from collections import defaultdict


graph = defaultdict(list)


# dfs approach로 route 탐색
# 탐색 후 모든 티켓을 사용하지 않았다면 다시 탐색
# visited를 사용하지 않고 그래프를 pop, insert해서 사용
def find_route(node, route, target):
    if len(route) == target:
        return route
    for idx, next_ in enumerate(graph[node]):
        keep = graph[node].pop(idx)
        ret = find_route(next_, route + [next_], target)
        graph[node].insert(idx, keep)
        if ret:
            return ret


# 그래프 생성
def make_graph(tickets):
    lim = len(tickets)
    graph = defaultdict(list)
    for i in range(lim):
        graph[tickets[i][0]].append(tickets[i][1])
    for key in graph.keys():
        graph[key].sort()
    return graph


def solution(tickets):
    global graph, route
    graph = make_graph(tickets)
    ret = find_route('ICN', ['ICN'], len(tickets) + 1)
    return ret