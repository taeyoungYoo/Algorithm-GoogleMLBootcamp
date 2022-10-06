'''
     프로그래머스 아이템 줍기
     - 지나갈 수 있는 경로만 1, 나머지는 0과 -1로 고정
     - bfs로 최단거리 확인
     - 좌표를 2배 스케일링해서 거리 분리 후 결과값 2로 나누기
'''
from collections import deque


# 전역변수 설정
lim = 101
min_r = 0
max_r = 100
min_c = 0
max_c = 100
rec_map = [[0] * lim for _ in range(lim)]


def make_map(rec):
    '''
    이동이 가능한 좌표를 rec_map에 표시
    -1 : 이동 불가(직사각형 내부)
    0 : 이동 불가(빈 좌표)
    1 : 이동 가능
    :param rec: 직사각형 좌표
    :return:
    '''
    global rec_map, min_r, max_r, min_c, max_c
    block = -1
    init_dist = 10001
    # scaling with factor 2
    for i in range(4):
        rec[i] *= 2
    min_r = min(min_r, rec[1])
    max_r = max(max_r, rec[3])
    min_c = min(min_c, rec[0])
    max_c = max(max_c, rec[2])
    for i in range(rec[0], rec[2]+1):
        if rec_map[rec[1]][i] != block:
            rec_map[rec[1]][i] = init_dist
        if rec_map[rec[3]][i] != block:
            rec_map[rec[3]][i] = init_dist
    for i in range(rec[1], rec[3]+1):
        if rec_map[i][rec[0]] != block:
            rec_map[i][rec[0]] = init_dist
        if rec_map[i][rec[2]] != block:
            rec_map[i][rec[2]] = init_dist
    for i in range(rec[0]+1, rec[2]):
        for j in range(rec[1]+1, rec[3]):
            rec_map[j][i] = block


def find_route(r, c, tar_r, tar_c):
    '''
    BFS를 통해 최소 루트 탐색
    :param r: 유저 y좌표
    :param c: 유저 x좌표
    :param tar_r: 아이템 y좌표
    :param tar_c: 아이템 x좌표
    :return: 아이템까지의 최소거리
    '''
    check = [0, -1]
    q = deque()
    q.append((r, c))
    rec_map[r][c] = 1
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    while q:
        r, c = q.popleft() # O(1)
        for i in range(4):
            n_r = r + dr[i]
            n_c = c + dc[i]
            if min_r <= n_r <= max_r and min_c <= n_c <= max_c and rec_map[n_r][n_c] not in check :
                if rec_map[r][c] + 1 < rec_map[n_r][n_c]:
                    rec_map[n_r][n_c] = rec_map[r][c] + 1
                    q.append((n_r, n_c))
    # 출발값이 1이니 1을 빼주고 2배 스케일링 했으니 2로 나눠주기기
    return (rec_map[tar_r][tar_c]-1) // 2


def solution(rectangle, characterX, characterY, itemX, itemY):
    for rec in rectangle:
        make_map(rec)
    characterY *= 2
    characterX *= 2
    itemY *= 2
    itemX *= 2
    answer = find_route(characterY, characterX, itemY, itemX)
    return answer