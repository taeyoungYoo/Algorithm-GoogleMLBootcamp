# 플로이드 워셜 전체탐색 
# 효율성 테스트 133.82ms ~ 1168.50ms 
'''
n : 노드의 개수
s : 출발지점
a : a 도착지점
b : b 도착지점
fares : [시작노드, 종료노드, 가격]
'''

import sys
INF = sys.maxsize 

# 플로이드 워셜 : 모든 노드 간 최단 경로 구성가능
def floyd(dist, n):
    # 3중 for문 O(n^3)
    for k in range(n): # 경유지 노드
        for i in range(n): # 출발지 노드
            for j in range(n): # 도착지 노드
                
                # dist[i][j] : i에서 j까지 가는 요금
                # dist[i][k] + dist[k][j]  : i에서 j까지 가는데 k를 경유해서 가는 경우 요금
                if dist[i][k] + dist[k][j] < dist[i][j]: # k를 경유해서 가는 요금이 싼 경우 
                    dist[i][j] = dist[i][k] + dist[k][j] # i->j 값을 업데이트 해준다. (최종적으로 최소 비용이 적용 됨)

def solution(n, s, a, b, fares):
    # 노드 및 노드간 요금 초기화
    dist = [[INF for _ in range(n)] for _ in range(n)] 
    for i in range(n):
        dist[i][i] = 0 # 자기자신은 요금이 0
    
    for edge in fares: 
        # 노드의 방향정보가 없기 때문에 양방향으로 같은 요금을 지정해준다.
        dist[edge[0]-1][edge[1]-1] = edge[2] 
        dist[edge[1]-1][edge[0]-1] = edge[2]
        
    # 플로이드 워셜 알고리즘
    floyd(dist, n)
    print(dist)
    
    # 문제에서는 노드번호가 1부터 시작하기 때문에 
    # 파이썬 인덱싱 번호에 맞춰 1씩 빼준다. 
    s -= 1
    a -= 1
    b -= 1
    
    answer = INF # 초기값
    
    for k in range(n):
        # dist[s][k] : s(시작노드)에서 k 까지(합승) 요금
        # dist[k][a] : 합습 종료지점에서 a지점 까지 요금
        # dist[k][b] : 합습 종료지점에서 b지점 까지 요금
        answer = min(answer, dist[s][k] + dist[k][a] + dist[k][b])  # 최소값 갱신
    
    return answer
