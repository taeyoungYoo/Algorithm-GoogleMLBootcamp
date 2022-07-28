# 해답 참고. : 메모리 42896 kb, 시간 256 ms
import heapq, sys


n, m = map(int, sys.stdin.readline().split())

problems = [0 for _ in range(n + 1)]                    # 우선 풀 문제가 있는지 체크할 리스트
pre_dict = {}                                           # 우선 풀 문제 딕셔너리
for _ in range(m):                                      # 먼저 풀어야 하는 문제 정보를 입력받아 pre_dict에 추가
    pre, post = map(int, sys.stdin.readline().split())
    problems[post] += 1                                 # 우선 풀 문제가 있는 경우 해당 문제 +1
    if pre in pre_dict:                                 # 먼저 풀어야 하는 문제가 pre_dict에 있는 경우 append
        pre_dict[pre].append(post)
    else:                                               # 먼저 풀어야 하는 문제가 pre_dict에 없는 경우 새로 생성
        pre_dict[pre] = [post]

que = []                                # 가장 먼저 풀어야 하는 문제들 que에 추가
for i in range(1, n+1):
    if problems[i] == 0:
        heapq.heappush(que, i)

answer = []
while que:                              # que 돌면서 answer에 풀어야하는 순서대로 문제를 쌓음
    i = heapq.heappop(que)
    answer.append(i)

    if i in pre_dict:
        for j in pre_dict[i]:
            problems[j] -= 1
            if problems[j] == 0:
                heapq.heappush(que, j)

print(*answer)
# expect: 3 1 4 2


# 풀이 1. fail
# pre_dict = {}
# for _ in range(cnt):
#     pre, post = map(int, sys.stdin.readline().split())
#     if pre in pre_dict:
#         pre_dict[pre].append(post)
#     else:
#         pre_dict[pre] = [post]
#
# problems = list(range(1, n + 1))
# problems = [x for x in problems if x not in pre_dict]
#
# rev_pre_dict = {}
# for k, v in pre_dict.items():
#     rev_pre_dict[v] = k
#
# while len(problems) > 0:
#
#     problem = problems.pop(0)
#     if problem in rev_pre_dict:
#         post = rev_pre_dict.get(problem)
#         print(problem, post, end=' ')
#     else:
#         print(problem, end=' ')
