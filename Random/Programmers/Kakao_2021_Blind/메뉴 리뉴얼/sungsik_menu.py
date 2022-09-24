from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []

    for c in course:
        combis = []

        for o in orders:
            combis.extend(list(combinations(sorted(o), c)))

        counter = Counter(combis)

        count = [i for i, v in counter.items() if v > 1 and max(counter.values()) == v]
        answer.extend(list(map(list, count)))

    return sorted(list(map(''.join, answer)))
