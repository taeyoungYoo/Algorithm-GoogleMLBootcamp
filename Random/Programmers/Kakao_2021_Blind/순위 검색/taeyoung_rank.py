import collections
from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer = []

    info_split = [x.split(' ') for x in info]
    query_split = [x.split(' ') for x in query]
    score_info = [int(x.pop()) for x in info_split]
    score_query = [int(x.pop()) for x in query_split]
    for i in range(len(query_split)):
        while True:
            try:
                query_split[i].remove('and')
            except:
                break
        query_split[i] = ''.join(query_split[i])

    info_dict = collections.defaultdict(list)

    for i in range(len(info_split)):
        for j in range(5):
            for combi in combinations(range(4), j):
                key_cand = []
                for k in range(4):
                    if k in combi:
                        key_cand.append('-')
                    else:
                        key_cand.append(info_split[i][k])
                info_dict[''.join(key_cand)].append(score_info[i])

    for key in info_dict.keys():
        info_dict[key].sort()

    for i in range(len(query_split)):
        target = score_query[i]
        if query_split[i] in info_dict.keys():
            answer.append(len(info_dict[query_split[i]]) - bisect_left(info_dict[query_split[i]], target))
        else:
            answer.append(0)
    return answer


# import collections
# from itertools import combinations
#
# def solution(info, query):
#     answer = []
#
#     info_split = [x.split(' ') for x in info]
#     query_split = [x.split(' ') for x in query]
#     score_info = [int(x.pop()) for x in info_split]
#     score_query = [int(x.pop()) for x in query_split]
#     for i in range(len(query_split)):
#         while True:
#             try:
#                 query_split[i].remove('and')
#             except:
#                 break
#         query_split[i] = ''.join(query_split[i])
#
#     info_dict = collections.defaultdict(list)
#
#     for i in range(len(info_split)):
#         for j in range(5):
#             for combi in combinations(range(4), j):
#                 key_cand = []
#                 for k in range(4):
#                     if k in combi:
#                         key_cand.append('-')
#                     else:
#                         key_cand.append(info_split[i][k])
#                 info_dict[''.join(key_cand)].append(score_info[i])
#
#     for key in info_dict.keys():
#         info_dict[key].sort()
#
#     for i in range(len(query_split)):
#         target = score_query[i]
#         cand = info_dict[query_split[i]]
#         ret = 0
#         for score in cand:
#             if score >= target:
#                 ret += 1
#         answer.append(ret)
#     return answer