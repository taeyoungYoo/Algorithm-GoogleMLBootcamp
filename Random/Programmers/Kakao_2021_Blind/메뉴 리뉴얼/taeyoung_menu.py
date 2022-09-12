# Kakao 2021 blind
# DFS를 활용해 주문 건마다 n개의 조합 개수를 구함
# Counter dictionary 활용 최대 주문 조합 return

import collections


def solution(orders, course):
    order_list = [list(x) for x in orders]
    for i in range(len(order_list)):
        order_list[i].sort()
    answer = []

    # 주문 조합 구하기
    def get_list(sub_list, idx, l, n):
        if len(l) == n:
            ret[''.join(l)] += 1
            return

        for i in range(idx, len(sub_list)):
            get_list(sub_list, i + 1, l + [sub_list[i]], n)

    # Course 개수 별 최대 조합 구하기
    for n in course:
        ret = collections.Counter()
        for sub_order in order_list:
            get_list(sub_order, 0, [], n)
        max_ret = max(ret.values(), default=0)
        if max_ret < 2:
            continue
        for key in ret.keys():
            if ret[key] == max_ret:
                answer.append(key)
    answer.sort()

    return answer