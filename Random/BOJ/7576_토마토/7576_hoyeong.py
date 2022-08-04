#참고 풀이 - 2156ms
'''
M x N(가로x세로) 사이즈의 토마토 상자가 있음
0 : 안익은 토마토
1 : 익은 토마토
-1 : 토마토 없음
1(익은토마토)를 기준으로 주변(상하좌우)의 0(안익은 토마토)를 
하루에 하나씩 익게 한다.
모든 박스의 토마토를 익히기 위해서 소요되는 일자
모든 박스를 익히지 못하면 -1 return

전
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
->

후
[[9, 8, 7, 6, 5, 4],
 [8, 7, 6, 5, 4, 3],
 [7, 6, 5, 4, 3, 2],
 [6, 5, 4, 3, 2, 1]]
'''
# 2156ms 
# bfs는 queue를 사용한다. 
from collections import deque
queue = deque([])

#입력
M, N = map(int, input().split())
tomato_box = [list(map(int, input().split())) for _ in range(N)]

#방향 리스트
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] #상, 하, 좌, 우 
res = 0

# 토마토 박스 전체 순회하면서
# 익은 토마토 찾아서, queue에 좌표 입력
for i in range(N):
    for j in range(M):
        if tomato_box[i][j] == 1:
            queue.append([i,j])

# bfs함수 - O(n^2) ??
def bfs():
    # 큐 안에 좌표가 남아있으면 하나씩
    # x,y가 헷갈릴 수 있겠다.
    while queue:
        x, y = queue.popleft() # 익은토마토 좌표 x,y에 입력
        for i in range(4): #상화좌우 순회
            nx, ny = x + dx[i], y + dy[i] # new_x, new_y 
            #범위 내에 안익은 토마토(0)이 있으면
            if (0 <= nx < N) and (0 <= ny < M) and (tomato_box[nx][ny] == 0): 
                # 토마토를 익히고 1씩 더해간다.
                tomato_box[nx][ny] = tomato_box[x][y] + 1
                # 큐에 갱신된 좌표를 입력한다.
                queue.append([nx,ny])

# 토마토 익히기
bfs()

# 상태확인을 위한 flag 변수선언
flag = 1

# 토마토박스 전체 돌면서 최대값  갱신
for i in tomato_box:
    res = max(res, max(i))
    # 안익은 토마토(0) 이 남아있다면 flag 0으로 
    if 0 in i:
        flag = 0

# flag 1이면       
if flag == 1:
    # res값 출력
    # 1부터 시작하니까 소요일자 계산을 위해 1을 빼준다. 
    print(res-1)
# flag 0이면 (0이 box에 남아있는 경우) -1 출력
else:
    print(-1)

    
   
