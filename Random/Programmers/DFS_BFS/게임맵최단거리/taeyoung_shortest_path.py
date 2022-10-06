'''
    프로그래머스 게임 맵 최단 거리
    - BFS로 최단거리를 찾아준다
'''

from collections import deque


# map을 최소값으로 초기화하고 푸는 approach
def bfs(maps):
    start = (0, 0)
    q = deque()
    q.append(start)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    lim_r = len(maps)
    lim_c = len(maps[0])
    while q:
        r, c = q.popleft()
        for i in range(len(dr)):
            nr = r + dr[i]
            nc = c + dc[i]
            update_val = maps[r][c] + 1
            if 0 <= nr < lim_r and 0 <= nc < lim_c and maps[nr][nc] != 0 and maps[nr][nc] > update_val :
                q.append((nr, nc))
                # maps[nr][nc] = min(maps[nr][nc], maps[r][c] + 1)
                maps[nr][nc] = maps[r][c] + 1
    return maps[-1][-1]


def solution(maps):
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 1:
                maps[i][j] = 10001
    maps[0][0] = 1
    ret = bfs(maps)
    if ret == 10001:
        return -1
    else:
        return ret

'''
    최소값 염두에 안두고 검사하는 BFS
'''
def bfs(maps):
    start = (0, 0)
    q = deque()
    q.append(start)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    lim_r = len(maps)
    lim_c = len(maps[0])
    while q:
        r, c = q.popleft()
        for i in range(len(dr)):
            nr = r + dr[i]
            nc = c + dc[i]
            update_val = maps[r][c] + 1
            if 0 <= nr < lim_r and 0 <= nc < lim_c and maps[nr][nc] != 0:
                if maps[nr][nc] == 1 or maps[nr][nc] > update_val:
                    q.append((nr, nc))
                    maps[nr][nc] = update_val
    return maps[-1][-1]


def solution(maps):
    ret = bfs(maps)
    if ret == 1:
        return -1
    else:
        return ret