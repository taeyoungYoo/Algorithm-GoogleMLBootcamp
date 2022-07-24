# BOJ 1766
# 순서 정하기 -> topology sort: O(V+E)
# N <= 32,000, M<= 100,000
# 일반적인 topology sort에서 우선순위 큐를 적용해서 순서를 맞춰준다
# 우선순위 큐: O(nlogn)

import heapq

n, m = map(int, input().split())
in_degree = [0] * (n + 1)
adj_list = [[] for i in range(n + 1)]
pq = []
ret = []

for i in range(m):
    tmp_1, tmp_2 = map(int, input().split())
    adj_list[tmp_1].append(tmp_2)
    in_degree[tmp_2] += 1

# init priority queue
for i in range(1, n + 1):
    if in_degree[i] == 0:
        heapq.heappush(pq, i)
# topology sort
while pq:
    cur = heapq.heappop(pq)
    ret.append(cur)
    for node in adj_list[cur]:
        in_degree[node] -= 1
        if in_degree[node] == 0:
            heapq.heappush(pq, node)

for data in ret:
    print(data, end=' ')