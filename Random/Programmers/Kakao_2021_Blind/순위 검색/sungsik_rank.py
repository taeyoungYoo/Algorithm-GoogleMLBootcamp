import re
from bisect import bisect_left
from itertools import combinations
from collections import defaultdict



info = ["java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100",
         "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250",
         "- and backend and senior and - 150",
         "- and - and - and chicken 100",
         "- and - and - and - 150"]

# expect : [1,1,1,1,2,4]

answer = []

dic = defaultdict(list)
for i in info:
    i = i.split()
    condition = i[:-1]
    score = int(i[-1])

    for j in range(5):
        case = list(combinations([0,1,2,3], j))

        for c in case:
            tmp = condition.copy()
            for idx in c:
                tmp[idx] = "-"
            key = ''.join(tmp)
            dic[key].append(score)

for value in dic.values():
    value.sort()

for q in query:
    q = q.replace("and ", "")
    q = q.split()
    target_key = ''.join(q[:-1])
    target_score = int(q[-1])
    count = 0

    if target_key in dic:
        target_list = dic[target_key]
        idx = bisect_left(target_list, target_score)
        count = len(target_list) - idx
    answer.append(count)

print(answer)

### 풀이 1: 효율성 0/4 (시간초과)
# def solution(info, query):
#     answer = []
#     info_s = [x.split(' ') for x in info]
#
#     for q in query:
#         l = q.split()[0]
#         end = q.split()[2]
#         career = q.split()[4]
#         food = q.split()[6]
#         score = q.split()[7]
#
#         candi = 0
#
#         for can in info_s:
#             can_l, can_end, can_career, can_food, can_score = can
#
#             if (l == '-' or l == can_l) and (end == '-' or end == can_end) and (career == '-' or career == can_career) and (food == '-' or food == can_food) and (int(can_score) >= int(score)):
#                 candi += 1
#
#         answer.append(candi)
#
#     return answer

### 풀이 2: 효율성 0/4 (시간초과)
# def solution(info, query):
#     answer = []
#     info_s = [x.split(' ') for x in info]
#     info_s = sorted(info_s, key=lambda x : int(x[4]))
#
#     for q in query:
#         l = q.split()[0]
#         end = q.split()[2]
#         career = q.split()[4]
#         food = q.split()[6]
#         score = int(q.split()[7])
#
#         candi = []
#
#         for can in info_s:
#             can_l, can_end, can_career, can_food, can_score = can
#
#             if (l == '-' or l == can_l) and (end == '-' or end == can_end) and (career == '-' or career == can_career) and (food == '-' or food == can_food):
#                 candi.append(int(can_score))
#
#         answer.append(len(candi) - bisect_left(candi, score))
#
#     return answer
