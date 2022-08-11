# 시간 2984 ms, 메모리 106140 kb
from collections import deque


m, n = 6, 4
graph = [[0,0,0,0,0,0],
         [0,0,0,0,0,0],
         [0,0,0,0,0,0],
         [0,0,0,0,0,1]]

que = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            # 익은 토마토(1)의 좌표를 큐에 저장
            que.append([i, j])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while que:
    x, y = que.popleft()
    for i in range(4):
        # 상하좌우 돌면서 일수 저장
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                que.append([nx, ny])

answer = 0
for line in graph:
    for tomato in line:
        if tomato == 0:
            # 안익은 토마토(0)이 있으면 정지
            print(-1)
            exit()
    answer = max(answer, max(line))

# 1에서 시작했기 때문에 결과 값에서 1빼주기
print(answer-1)
