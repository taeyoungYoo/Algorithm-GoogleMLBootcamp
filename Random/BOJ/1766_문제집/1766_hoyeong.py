# 내풀이 - 시간초과

# 입력
# 1. N : 문제의 수, M : 먼저 푸는 문제 정보 개수
# 2. M개의 줄에 걸쳐 두 정수의 순서쌍 (A,B)
import sys
input = sys.stdin.readline

# M개의 줄에 걸쳐
# 입력 1 
N, M = map(int, input().split())

# 입력 2 - M개의 줄에 걸쳐 두 정수의 순서쌍 A,B
tmp = []
for _ in range(M):   # O(n)
    A, B = input().split()  
    tmp.append([A,B])  # [[4,2],[3,1]

tmp.sort() # O(nlogn)   -> [[3,1],[4,2]]
tmp = sum(tmp,[]) # O(n)  flatten효과 -> [3,1,4,2]
#출력
print(*tmp) # 3 1 4 2

# --------------------------------- 

# 위상정렬(구글링 풀이) -  252ms
# 위상정렬 진입차수가 0인 원소부터 탐색
from heapq import *
# 노드의 개수가 간선의 개수를 입력 받기
v,e = map(int, input().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v+1)    
# 각 노드에 연결된 간선(노드간 화살표) 정보를 담기 위한 연결 리스트 초기화
graph = [[] for i in range(v+1)]

# 방향 그래프의 모든 간선 정보를 입력 받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # 정점 A에서 B로 이동 가능
    # 진입 차수를 1 증가
    indegree[b] += 1
    # print(indegree) # [0, 1, 1, 0, 0]
    # print(graph) #  [[], [], [], [1], [2]]

result = [] # 결과 담는 리스트
heap = [] # 우선순위 큐
for i in range(1, v+1): # O(n)  - 1번부터 시작하려고 +1 하는 것임
    if indegree[i] == 0:  # 진입차수가 0이면
        heappush(heap, i) # heap에 index 넣는다 [] -> [3] -> [3,4]

while heap: # O(n)
    now = heappop(heap)  # 숫자가 가장 낮은 값을 now 에 pop 한다  heap : [3, 4] -> [4]
    result.append(now)   # result에 추가   [3] 
    for i in graph[now]: # graph[3] -> 1
        indegree[i] -= 1  #  indegree [0,1,1,0,0] -> [0,0,1,0,0]
        if indegree[i] == 0:  # indegree[1] -> 0
            heappush(heap, i)  # heappush(heap, 1) : [4] -> [1,4]  이후 과정 반복 heap이 result에 모두 더해질때 까지
print(*result)
