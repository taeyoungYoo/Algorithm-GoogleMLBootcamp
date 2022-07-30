# 백준 7576 토마토
# runtime: 1760, memory: 106200KB
# linked array : O(N*M) -> 1,000,000

import collections

m, n = map(int, input().split())
tomato = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(n):
    tomato.append(list(map(int, input().split())))
q = collections.deque()
is_full = True

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            q.append([i, j])
        elif tomato[i][j] == 0:
            is_full = False


def bfs():
    while q:
        cur_row, cur_col = q.popleft()
        for i in range(4):
            next_row = cur_row + dy[i]
            next_col = cur_col + dx[i]
            if 0 <= next_row < n and 0 <= next_col < m and tomato[next_row][next_col] == 0:
                tomato[next_row][next_col] = tomato[cur_row][cur_col] + 1
                q.append([next_row, next_col])


if is_full:
    print(0)
else:
    bfs()
    ret = 0
    is_left = False
    for i in range(n):
        for j in range(m):
            ret = max(ret, tomato[i][j])
            if tomato[i][j] == 0:
                is_left = True
    if is_left:
        print(-1)
    else:
        print(ret-1)
