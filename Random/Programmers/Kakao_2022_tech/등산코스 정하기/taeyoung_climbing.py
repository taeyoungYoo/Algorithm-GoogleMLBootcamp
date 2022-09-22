

'''
 2022 Kakao Internship 등산코스 정하기
 Dijkstra 변형
   - 최단거리 업데이트가 아닌 현재 노드까지의 max intensity로 업데이트
   - 한 번에 모든 노드에 대한 max intensity 구하기
   - O(Elog(V))
'''

import heapq

INF = 987654321

def dijkstra(n, graph, gates, summits):
    # 최단 거리 배열
    intensity = [INF] * (n + 1)
    # 처리 노드 관리 우선순위 큐
    q = []
    ret = []
    # 모든 출발 지점을 큐에 추가
    # 한 번에 노드 간 최대 intensity 계산
    for gate in gates:
        heapq.heappush(q, (0, gate))
        intensity[gate] = 0

    while q:
        cur_cost, cur_node = heapq.heappop(q)
        # 가져온 노드까지의 intensity가 cost보다 작다면 업데이트 필요 없음
        if intensity[cur_node] < cur_cost:
            continue
        if cur_node in summits:
            ret.append((cur_cost, cur_node))
            continue
        # 인접 노드 검사
        for next in graph[cur_node]:
            new_intensity, new_node = next[0], next[1]
            # 기존 intensity와 인접 노드까지의 거리를 비교해 max로 업데이트
            if intensity[new_node] > max(new_intensity, cur_cost):
                intensity[new_node] = max(new_intensity, cur_cost)
                heapq.heappush(q, (intensity[new_node], new_node))
    return ret

def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n + 1)]
    for path in paths:
        graph[path[0]].append((path[2], path[1]))
        graph[path[1]].append((path[2], path[0]))
    dist = dijkstra(n, graph, gates, summits)
    dist.sort()
    answer = [dist[0][1], dist[0][0]]
    return answer