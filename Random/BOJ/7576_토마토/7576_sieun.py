# 참고: https://jae04099.tistory.com/entry/%EB%B0%B1%EC%A4%80-7576-%ED%86%A0%EB%A7%88%ED%86%A0-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%95%B4%EC%84%A4%ED%8F%AC%ED%95%A8

from collections import deque

# input
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

answer = 0
q = deque([])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 익은 토마토 좌표를 큐에 추가 
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i, j))

# bfs 
def bfs():
    while q:
        # 익은 토마토 좌표 pop
        x, y = q.popleft()
        # 인접 토마토 익히기 
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 범위 안에 속하며, 익지 않은 토마토인 경우
            if nx in range(0, n) and ny in range(0, m) and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append([nx, ny])

bfs()

answer = 0

for row in graph:
    # 익지 않은 토마토가 존재
    if 0 in row:
        answer = -1
        break
    else:
        answer = max(answer, max(row))

# 시작이 0이 아닌 1이므로 1을 빼줌
if answer > 0:
    answer -= 1

print(answer)
